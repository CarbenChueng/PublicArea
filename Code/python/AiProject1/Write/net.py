import torch
from torch import nn


class NetV1(nn.Module):

    # 网络的结构进行构造
    def __init__(self):
        super().__init__()

        self.w = nn.Parameter(torch.randn(784, 10))  # randn是正态分布的随机数

    # 网络前向过程的逻辑
    def forward(self, x):
        h = x @ self.w
        # print(self.w.dtype)

        # softmax
        h = torch.exp(h)
        z = torch.sum(h, dim=1, keepdim=True)  # 0是行,1是列
        return h / z


class NetV2(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(784, 100)
        self.relu = nn.ReLU()

        self.fc2 = nn.Linear(100, 52)
        self.fc3 = nn.Linear(52, 10)
        self.softMax = nn.Softmax(dim=1)

    def forward(self, x):
        h = self.fc1(x)
        h = self.relu(h)
        h = self.fc2(h)
        h = self.relu(h)
        h = self.fc3(h)
        out = self.softMax(h)
        return out


class NetV3(nn.Module):
    def __init__(self):
        super().__init__()
        self.layer = nn.Sequential(nn.Linear(784,100),
                                   nn.ReLU(),
                                   nn.Linear(100,52),
                                   nn.ReLU(),
                                   nn.Linear(52, 10),
                                   nn.Softmax(dim=1),
                                   )

class Netv6(nn.Module):
    def __init__(self):
        super().__init__()
        self.layers = nn.Sequential(
            nn.Conv2d(1, 16, 3, padding=1),
            nn.ReLU(),
            nn.Conv2d(16, 32, 3, 2, padding=1),
            nn.ReLU(),
            nn.Conv2d(32, 64, 3, 2, padding=1),
            nn.ReLU()

        )

    def forward(self, x):
        return self.layer(x)


if __name__ == '__main__':
    net = NetV3()
    x = torch.randn(6, 784)
    y = net(x)
    print(y.shape)
