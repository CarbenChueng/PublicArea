import torch
from torch import nn

class Netv6(nn.Module):
    def __init__(self):
        super().__init__()
        self.layer = nn.Sequential(
            nn.Conv2d(3, 32, 3),
            nn.MaxPool2d(3),
            nn.ReLU(),

            nn.Conv2d(32, 64, 3),
            nn.MaxPool2d(3,2),
            nn.ReLU(),

            nn.Conv2d(64, 128, 3),
            nn.ReLU(),

            nn.Conv2d(128, 256, 3),
            nn.ReLU(),

            nn.Conv2d(256, 512, 3),
            nn.ReLU(),

            nn.Conv2d(512, 1024, 3),
            nn.ReLU(),
        )

        self.outLayer = nn.Sequential(
            nn.Linear(1024*6*6,2),
            nn.Softmax(dim=1)

        )

    def forward(self, x):
        h = self.layer(x)
        # print(x)
        # print(h.shape)
        h = h.reshape(-1,1024*6*6)
        out = self.outLayer(h)
        # print(type(out))
        return out

if __name__ == '__main__':
    net = Netv6()
    x = torch.randn(1,3,100,100)
    y = net(x)
    print(y.shape)