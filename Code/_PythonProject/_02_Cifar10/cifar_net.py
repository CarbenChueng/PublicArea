from torch.nn import *
import torch


class Net(Module):


    def __init__(self):
        super(Net, self).__init__()
        self.layers = Sequential(
            Linear(32*32*3,1500),
            PReLU(),
            Linear(1500,750),
            PReLU(),
            Linear(750,375),
            PReLU(),
            Linear(375,150),
            PReLU(),
            Linear(150,10),
            # PReLU(),
            Softmax(dim=1)

        )

    def forward(self,x):
        return self.layers(x)

if __name__ == '__main__':
    net = Net()
    x = torch.randn(6,32*32*3)
    y = net(x)
    print(y.shape)

