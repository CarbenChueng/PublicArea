from torchvision import datasets,transforms
from torch.utils.data import DataLoader

train_dataset = datasets.MNIST(root="data/MNIST_data",train=True,transform=transforms.ToTensor(),download=True)
test_dataset = datasets.MNIST(root="data/MNIST_data",train=False,transform=transforms.ToTensor(),download=False)

# print(train_dataset.data.shape)
# print(train_dataset.targets.shape)
# print(train_dataset.data[0])
# print(train_dataset.targets[0])
# print(test_dataset.data.shape)
# print(test_dataset.targets.shape)
#
# img = train_dataset.data[0]
uncode = transforms.ToPILImage()
# img = uncode(img)
# print(type(img))
# img.show()

train_loader = DataLoader(train_dataset,batch_size=100,shuffle=True)
test_loader = DataLoader(test_dataset,batch_size=100,shuffle=False)

for i,(img,label) in enumerate(train_loader):
    img = uncode(img[0])
    img.show()