import torch
from torch import nn


if __name__ == '__main__':
    conv = nn.Conv2d(3,16,(3,2),1)#(输入通道,输出通道,核的大小,步长)
    x = torch.randn(1,3,16,16)#NCHW
    y = conv(x)
    print(y.shape)