import os
from PIL import Image
import torch.utils.data as data
import torchvision.transforms as transforms

class CustomDataset(data.Dataset):
    def __init__(self, root_dir, transform=None):
        self.root_dir = root_dir
        self.transform = transform
        self.classes, self.class_to_idx = self._find_classes(self.root_dir)
        self.samples = self._make_dataset(self.root_dir, self.class_to_idx)
        
    def __getitem__(self, index):
        path, target = self.samples[index]
        img = Image.open(path).convert('L')
        if self.transform is not None:
            img = self.transform(img)
        return img, target
    
    def __len__(self):
        return len(self.samples)
    
    def _find_classes(self, dir):
        classes = [d for d in os.listdir(dir) if os.path.isdir(os.path.join(dir, d))]
        classes.sort()
        class_to_idx = {classes[i]: i for i in range(len(classes))}
        return classes, class_to_idx
    
    def _make_dataset(self, dir, class_to_idx):
        images = []
        for target_class in os.listdir(dir):
            if not os.path.isdir(os.path.join(dir, target_class)):
                continue
            target = class_to_idx[target_class]
            target_dir = os.path.join(dir, target_class)
            for root, _, fnames in sorted(os.walk(target_dir)):
                for fname in fnames:
                    path = os.path.join(root, fname)
                    item = (path, target)
                    images.append(item)
        return images