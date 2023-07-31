import torch
from torch.nn import *


class Net(Module):

    def __init__(self):
        super(Net, self).__init__()
        self.layers = Sequential(
            Linear(784,398),
            PReLU(),
            Linear(398,10),
            Softmax()
        )

    #网络前向计算
    def forward(self,x):
        return self.layers(x)

if __name__ == '__main__':
    net = Net()
    x = torch.randn([3,784])
    y = net(x)
    print(y.shape)