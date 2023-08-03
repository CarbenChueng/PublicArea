from torch.nn import *
import torch

class Net(Module):

    def __init__(self):
        super(Net, self).__init__()
        self.layers = Sequential(
            Conv2d(3,12,3),
            LeakyReLU(),
            MaxPool2d(2),
            Conv2d(12,24,3),
            # MaxPool2d(2),
            LeakyReLU(),
            Conv2d(24,32,3),
            LeakyReLU(),
            Conv2d(32,54,3),
            LeakyReLU(),
            Conv2d(54,62,3),
            LeakyReLU(),
            Conv2d(62,87,3),
            LeakyReLU(),

        )

        self.out_layers = Sequential(
            Linear(87*5*5,10),
            # Softmax(dim=1)
        )

    def forward(self,x):
        x = self.layers(x)
        x = x.reshape(-1,87*5*5)
        return self.out_layers(x)

if __name__ == '__main__':
    net = Net()
    x = torch.randn(6,3,32,32)
    y = net(x)
    print(y.shape)

