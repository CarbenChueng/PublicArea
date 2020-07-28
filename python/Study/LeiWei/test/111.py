from torchvision import datasets

cifar10 = datasets.CIFAR10("wd",download=True)
print(cifar10.shape)