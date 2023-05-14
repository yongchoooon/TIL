import os
import argparse
import torch
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt

from data import CustomDataset
from model import MLP


from torchvision.transforms import RandomCrop, RandomHorizontalFlip, ToTensor
from torchvision import transforms


# Set random seed for reproducibility
torch.manual_seed(42)

# Define command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--batch_size', type=int, default=32, help='batch size')
parser.add_argument('--num_epochs', type=int, default=50, help='number of epochs')
parser.add_argument('--learning_rate', type=float, default=0.01, help='learning rate')
parser.add_argument('--momentum', type=float, default=0.9, help='momentum')
parser.add_argument('--weight_decay', type=float, default=0, help='weight decay')
args = parser.parse_args()

# Define hyperparameters
batch_size = args.batch_size
num_epochs = args.num_epochs
learning_rate = args.learning_rate
momentum = args.momentum
weight_decay = args.weight_decay
patience = 10

# Define data transforms
train_transform = transforms.Compose([
    RandomCrop(28, padding=4),
    RandomHorizontalFlip(),
    ToTensor(),
])
val_transform = transforms.Compose([
    ToTensor(),
])
test_transform = transforms.Compose([
    ToTensor(),
])

# Create datasets
train_data = CustomDataset('data/notMNIST_small/train', transform=train_transform)
val_data = CustomDataset('data/notMNIST_small/val', transform=val_transform)
test_data = CustomDataset('data/notMNIST_small/test', transform=test_transform)

# Create data loaders
train_loader = torch.utils.data.DataLoader(train_data, batch_size=batch_size, shuffle=True)
val_loader = torch.utils.data.DataLoader(val_data, batch_size=batch_size)
test_loader = torch.utils.data.DataLoader(test_data, batch_size=batch_size)

# Create model
input_dim = 28 * 28
layer_dims = [100, 50, 25]
output_dim = 10
model = MLP(input_dim, layer_dims, output_dim)

# Define loss function and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=learning_rate, momentum=momentum, weight_decay=weight_decay)

# Train the model
best_val_acc = 0
patience_count = 0
train_losses, val_losses, train_accs, val_accs = [], [], [], []

for epoch in range(num_epochs):
    # Training
    train_loss = 0
    train_total = 0
    train_correct = 0
    
    model.train()
    for images, labels in train_loader:
        optimizer.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        train_loss += loss.item() * labels.size(0)
        _, predicted = torch.max(outputs.data, 1)
        train_total += labels.size(0)
        train_correct += (predicted == labels).sum().item()
    
    train_losses.append(train_loss / train_total)
    train_accs.append(train_correct / train_total)
    
    # Validation
    val_loss = 0
    val_total = 0
    val_correct = 0
    
    model.eval()
    with torch.no_grad():
        for images, labels in val_loader:
            outputs = model(images)
            loss = criterion(outputs, labels)
            val_loss += loss.item() * labels.size(0)
            _, predicted = torch.max(outputs.data, 1)
            val_total += labels.size(0)
            val_correct += (predicted ==labels).sum().item()
    
    val_losses.append(val_loss / val_total)
    val_acc = val_correct / val_total
    val_accs.append(val_acc)
    
    # Save best model
    if val_acc > best_val_acc:
        best_val_acc = val_acc
        best_model = model.state_dict()
        best_epoch = epoch
        patience_count = 0
    else:
        patience_count += 1
    
    # Print progress
    print('Epoch [{}/{}], Train Loss: {:.4f}, Train Acc: {:.4f}, Val Loss: {:.4f}, Val Acc: {:.4f}'
          .format(epoch+1, num_epochs, train_loss/train_total, train_correct/train_total, val_loss/val_total, val_acc))
    
    # Early stopping
    if patience_count >= patience:
        print('Validation accuracy did not improve for {} epochs. Training stopped.'.format(patience))
        break
        
    # Save model weights for current epoch
    torch.save(model.state_dict(), os.path.join('models', 'epoch_{}.pt'.format(epoch+1)))
    
    # Generate plot every 5 epochs
    if (epoch+1) % 5 == 0:
        plt.plot(train_losses, label='train loss')
        plt.plot(val_losses, label='val loss')
        plt.plot(train_accs, label='train acc')
        plt.plot(val_accs, label='val acc')
        plt.legend()
        plt.savefig(os.path.join('results', 'epoch_{}.png'.format(epoch+1)))
        plt.close()

# Save best model
torch.save(best_model, os.path.join('models', 'best_epoch_{}.pt'.format(best_epoch+1)))

# Print final results
print('Best validation accuracy: {:.4f} (epoch {})'.format(best_val_acc, best_epoch+1))