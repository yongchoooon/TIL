import os
import random
import shutil

# Set random seed for reproducibility
random.seed(42)

# Define paths
data_path = 'data/notMNIST_small'
train_path = os.path.join(data_path, 'train')
val_path = os.path.join(data_path, 'val')
test_path = os.path.join(data_path, 'test')

# Create train, validation, and test directories for each alphabet
for alphabet in os.listdir(data_path):
    alphabet_path = os.path.join(data_path, alphabet)
    train_alphabet_path = os.path.join(train_path, alphabet)
    val_alphabet_path = os.path.join(val_path, alphabet)
    test_alphabet_path = os.path.join(test_path, alphabet)
    os.makedirs(train_alphabet_path, exist_ok=True)
    os.makedirs(val_alphabet_path, exist_ok=True)
    os.makedirs(test_alphabet_path, exist_ok=True)

    # Shuffle images
    images = os.listdir(alphabet_path)
    random.shuffle(images)

    # Split images into train, validation, and test sets
    num_images = len(images)
    num_train = int(0.7 * num_images)
    num_val = int(0.1 * num_images)
    num_test = num_images - num_train - num_val

    train_images = images[:num_train]
    val_images = images[num_train:num_train+num_val]
    test_images = images[num_train+num_val:]

    # Move images to appropriate directories
    for image in train_images:
        src_path = os.path.join(alphabet_path, image)
        dst_path = os.path.join(train_alphabet_path, image)
        shutil.move(src_path, dst_path)

    for image in val_images:
        src_path = os.path.join(alphabet_path, image)
        dst_path = os.path.join(val_alphabet_path, image)
        shutil.move(src_path, dst_path)

    for image in test_images:
        src_path = os.path.join(alphabet_path, image)
        dst_path = os.path.join(test_alphabet_path, image)
        shutil.move(src_path, dst_path)