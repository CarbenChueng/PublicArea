import torch
from torch import nn

class Net_v1(nn.Module):
    def __init__(self):
        super().__init__()
        self.layre = nn.Sequential(
            nn.Linear(784,512),
            nn.LeakyReLU(),
            nn.Linear(512,256),
            nn.LeakyReLU(),

            nn.Linear(256,128),
            nn.LeakyReLU(),
            nn.Linear(128,64),
            nn.LeakyReLU(),
            nn.Linear(64,10),

            nn.Softmax(dim=1)
        )

    def forward(self,x):
        return self.layre(x)

class Net_v2(nn.Module):
    def __init__(self):
        super().__init__()
        self.layre = nn.Sequential(
            nn.Conv2d(1,16,3,padding=1,bias=False),
            nn.MaxPool2d(2),
            nn.LeakyReLU(),
            nn.Conv2d(16,32,3),
            nn.MaxPool2d(2),
            nn.LeakyReLU(),
            nn.Conv2d(32,64,3),
            nn.LeakyReLU(),
        )
        self.output_layer = nn.Sequential(
            nn.Linear(64*4*4,10),
            nn.Softmax(dim=1)
        )

    def forward(self,x):
        h = self.layre(x)
        h = h.reshape(-1,64*4*4)
        h = self.output_layer(h)
        # print(h.shape)

        return h

if __name__ == '__main__':
    net = Net_v2()
    x = torch.rand(1,1,28,28)
    y = net(x)
    print(y.shape)
