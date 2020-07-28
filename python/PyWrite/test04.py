import torch
from torch import nn


if __name__ == '__main__':
    conv = nn.Conv2d(3,16,3,1,padding=1)
    x = torch.randn(1,3,24,16)#NCHW
    y = conv(x)
    print(y.shape)