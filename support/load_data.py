# Import libraries
import os

import torch
from torch.utils.data import DataLoader
from torchvision import datasets, transforms


def load_dataset(path_to_directory: str, random_seed=None, batch_size=1, transform=None):
    test_dir = "SteelBlastQC/test"
    train_dir = "SteelBlastQC/train"

    if transform is None:
        transform = transforms.Compose([transforms.ToTensor()])

    if random_seed is not None:
        torch.manual_seed(random_seed)
        torch.cuda.manual_seed(random_seed)

    train_path = os.path.join(path_to_directory, train_dir)
    train_dataset = datasets.ImageFolder(root=train_path, transform=transform)
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)

    test_path = os.path.join(path_to_directory, test_dir)
    test_dataset = datasets.ImageFolder(root=test_path, transform=transform)
    test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)

    return train_loader, test_loader, train_dataset, test_dataset

