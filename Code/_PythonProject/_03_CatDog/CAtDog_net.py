from torch.nn import *
from thop import profile,clever_format
import torch

class Net(Module):

    def __init__(self):
        super(Net, self).__init__()
        self.layers = Sequential(
            Conv2d(3,12,3),
            MaxPool2d(2),
            LeakyReLU(),
            Conv2d(12,24,3),
            MaxPool2d(2),
            LeakyReLU(),
            Conv2d(24,32,3),
            MaxPool2d(2),
            LeakyReLU(),
            Conv2d(32,54,3),
            LeakyReLU(),
            Conv2d(54,62,3),
            LeakyReLU(),

        )

        self.out_layer = Sequential(
            Linear(62*6*6,2)
            # Softmax(dim = 1)
        )

    #网络前向计算
    def forward(self,x):
        x = self.layers(x)
        x = x.reshape(-1,62*6*6)
        return self.out_layer(x)
        # return x

if __name__ == '__main__':
    net = Net()
    x = torch.randn(6,3,100,100)
    out = net(x)
    print(out.shape)
    # flops,paraam = profile(net,(x,))
    # flops, paraam = clever_format([flops, paraam], "%.3f")
    # print(flops,paraam,sep="\n")