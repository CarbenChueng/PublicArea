import torch
from torch.nn import *


class Net(Module):

    def __init__(self):
        super(Net, self).__init__()
        self.layers = Sequential(
            Linear(784,500),
            PReLU(),
            Linear(500,300),
            PReLU(),
            Linear(300,100),
            PReLU(),
            Linear(100,10)
,           Softmax(dim=1)
        )

    #网络前向计算
    def forward(self,x):
        return self.layers(x)

if __name__ == '__main__':
    net = Net()
    x = torch.randn([6,784])
    y = net(x)
    print(y.shape)