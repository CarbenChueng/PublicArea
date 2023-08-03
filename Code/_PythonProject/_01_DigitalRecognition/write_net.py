import torch
from torch.nn import *


class Net(Module):

    def __init__(self):
        super(Net, self).__init__()
        self.layers = Sequential(
            Conv2d(1,16,3),
            MaxPool2d(2),
            PReLU(),
            Conv2d(16,32,3),
            PReLU(),
            Conv2d(32,64,3),
            PReLU(),
        )

        self.out_layer = Sequential(
            Linear(64*9*9,10),
            Softmax(dim = 1)
        )

    #网络前向计算
    def forward(self,x):
        x = self.layers(x)
        x = x.reshape(-1,64*9*9)
        return self.out_layer(x)

if __name__ == '__main__':
    net = Net()
    x = torch.randn((1,1,28,28))
    y = net(x)
    print(y.shape)