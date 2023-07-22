import torch
import torch.nn as nn
import torch.nn.functional as F

class PNet(nn.Module):
    def __init__(self):
        super(PNet, self).__init__()
        self.pre_layer = nn.Sequential(
            nn.Conv2d(3,10,3,padding=1),
            nn.PReLU(),
            nn.MaxPool2d(kernel_size=3,stride=2),
            nn.Conv2d(10,16,3,1),
            nn.PReLU(),
            nn.Conv2d(16,32,3,1),
            nn.PReLU()
        )
        self.con4_1 = nn.Conv2d(32,1,1,1)
        self.con4_2 = nn.Conv2d(32,4,1,1)

    def forward(self,x):
        x = self.pre_layer(x)
        cond = torch.sigmoid(self.con4_1(x))
        offset = self.con4_2(x)
        return cond,offset

class RNet(nn.Module):
    def __init__(self):
        super(RNet, self).__init__()
        self.pre_layer = nn.Sequential(
            nn.Conv2d(3,28,3,padding=1),
            nn.PReLU(),
            nn.MaxPool2d(kernel_size=3,stride=2),
            nn.Conv2d(28,48,3,1),
            nn.PReLU(),
            nn.MaxPool2d(kernel_size=3,stride=2),
            nn.Conv2d(48,64,2,1),
            nn.PReLU()
        )
        self.con4 = nn.Linear(64*3*3,128)
        self.prelu4 = nn.PReLU()
        self.con5_1 = nn.Linear(128,1)
        self.con5_2 = nn.Linear(128,4)

    def forward(self,x):
        x = self.pre_layer(x)
        x = x.reshape(x.size(0),-1)
        x = self.con4(x)
        x = self.prelu4(x)
        label = torch.sigmoid(self.con5_1(x))
        offset = self.con5_2(x)
        return label,offset

class ONet(nn.Module):
    def __init__(self):
        super(ONet, self).__init__()
        self.pre_layer = nn.Sequential(
            nn.Conv2d(3,32,3,padding=1),
            nn.PReLU(),
            nn.MaxPool2d(kernel_size=3,stride=2),
            nn.Conv2d(32,64,3,1),
            nn.PReLU(),
            nn.MaxPool2d(kernel_size=3,stride=2),
            nn.Conv2d(64,64,3,1),
            nn.PReLU(),
            nn.MaxPool2d(kernel_size=2,stride=2),
            nn.Conv2d(64,128,2,1),
            nn.PReLU()
        )
        self.con5 = nn.Linear(128*3*3,256)
        self.prelu5 = nn.PReLU()
        self.con6_1 = nn.Linear(256,1)
        self.con6_2 = nn.Linear(256,4)

    def forward(self,x):
        x = self.pre_layer(x)
        x = x.reshape(x.size(0),-1)
        x = self.con5(x)
        x = self.prelu5(x)
        label = torch.sigmoid(self.con6_1(x))
        offset = self.con6_2(x)
        return label,offset

if __name__ == '__main__':
    p_net = PNet()
    r_net = RNet()
    o_net = ONet()

    x1 = torch.randn(1,3,12,12)
    x2 = torch.randn(1,3,24,24)
    x3 = torch.randn(1,3,48,48)
    print(p_net(x1))
    print(r_net(x2))
    print(o_net(x3))
