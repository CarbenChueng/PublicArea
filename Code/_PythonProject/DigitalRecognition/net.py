import torch
from torch.nn import *

class Net_v1(Module):

    def __init__(self):
        super(Net_v1, self).__init__()
        self.fc1 = Linear(784,500)
        self.relu = ReLU()
        self.fc2 = Linear(500,10)
        self.scm = Softmax(dim=1)

    def forward(self,x):
        h = self.fc1(x)
        h = self.relu(h)
        h = self.fc2(h)
        return self.scm(h)

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