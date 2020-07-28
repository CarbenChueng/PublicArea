from torch import nn
import torch


class Netv1(nn.Module):
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

        self.ouPutLayrt = nn.Sequential(
            nn.Linear(64 * 7 * 7, 10),  # 这层全链接就为了融合特征

            nn.Softmax(dim=1)

        )

    def forward(self, x):
        h = self.layers(x)
        # print(h.shape)
        h = h.reshape(-1, 64 * 7 * 7)  # NVHWE-->NV
        ouy = self.ouPutLayrt(h)
        return ouy


class Netv2(nn.Module):
    def __init__(self):
        super().__init__()
        self.layers = nn.Sequential(
            nn.Conv2d(1, 16, 3, padding=1,bias=False),
            nn.MaxPool2d(2),
            nn.ReLU(),

            nn.Conv2d(16, 32, 3),
            nn.MaxPool2d(2),
            nn.ReLU(),

            nn.Conv2d(32, 64, 3),
            nn.ReLU()

        )

        self.ouPutLayrt = nn.Sequential(
            nn.Linear(64*3*3, 10),  # 这层全链接就为了融合特征

            nn.Softmax(dim=1)

        )

    def forward(self, x):
        h = self.layers(x)
        # print(h.shape)
        h = h.reshape(-1,64*3*3)
        return self.ouPutLayrt(h)


if __name__ == '__main__':
    # net = Netv1()
    # x = torch.randn(3, 1, 26, 26)
    # y = net(x)
    # print(y.shape)

    net = Netv2()
    x = torch.randn(3, 1, 26, 26)
    y = net(x)
    print(y.shape)


    #卷积
    # con = nn.Conv2d(3,1,1,padding=1,bias=False)
    #
    # x = torch.randn(1,3,3,3)#NCHW
    # x1 = torch.randn(1,3,23,13)#NCHW
    # # print(x)
    # out = con(x)
    # out1 = con(x1)
    # # print(con.weight)
    # print(out.shape)
    # print(out1.shape)

    # con = nn.Conv2d(1, 1,3,1 ,dilation=1)
    # x = torch.randn(1,1,7,7)#NCHW
    # print(x)
    # out = con(x)
    # print(con.weight)
    # print(out.shape)
