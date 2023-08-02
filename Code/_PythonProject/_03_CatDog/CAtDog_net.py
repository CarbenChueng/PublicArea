from torch.nn import *
import torch

class Net(Module):

    def __init__(self):
        super(Net, self).__init__()
        self.layers = Sequential(
            Conv2d(3,16,3),
            MaxPool2d(2),
            PReLU(),
            Conv2d(16,32,3),
            MaxPool2d(2),
            PReLU(),
            Conv2d(32,64,3),
            PReLU(),
            Conv2d(64,128,3),
            PReLU(),
        )

        self.out_layer = Sequential(
            Linear(128*19*19,2),
            Softmax(dim = 1)
        )

    #网络前向计算
    def forward(self,x):
        x = self.layers(x)
        x = x.reshape(-1,128*19*19)
        return self.out_layer(x)
        # return self.layers(x)

if __name__ == '__main__':
    net = Net()
    x = torch.randn((1,3,100,100))
    out = net(x)
    print(out.shape)