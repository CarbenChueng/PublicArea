import torch
from torch import nn
from math import sqrt,exp

class Netv3(nn.Module):
    def __init__(self):
        super().__init__()
        self.layer = nn.Sequential(
            nn.Linear(10000,100),
            nn.ReLU(),
            nn.Linear(100,500),
            nn.ReLU(),
            nn.Linear(500,350),
            nn.ReLU(),
            nn.Linear(350,200),
            nn.ReLU(),
            nn.Linear(200,100),
            nn.ReLU(),
            nn.Linear(100,60),
            nn.ReLU(),
            nn.Linear(60,2),

            nn.Softmax(dim=1)
        )
    def forward(self,x):
        return self.layer(x)

class NetV2(nn.Module):
    def __init__(self):
        super().__init__()
        self.w1 = nn.Parameter(torch.randn(10000,1200)*sqrt(2/10000))
        self.b1 = nn.Parameter(torch.zeros(1200))
        self.w2 = nn.Parameter(torch.randn(1200, 800) * sqrt(2 / 1200))
        self.b2 = nn.Parameter(torch.zeros(800))
        self.w3 = nn.Parameter(torch.randn(800, 600) * sqrt(2 / 800))
        self.b3 = nn.Parameter(torch.zeros(600))
        self.w4 = nn.Parameter(torch.randn(600, 400) * sqrt(2 / 600))
        self.b4 = nn.Parameter(torch.zeros(400))
        self.w5 = nn.Parameter(torch.randn(400, 100) * sqrt(2 / 400))
        self.b5 = nn.Parameter(torch.zeros(100))
        self.w6 = nn.Parameter(torch.randn(100, 1) * sqrt(2 / 100))
        self.b6 = nn.Parameter(torch.zeros(2))
        self.actfunc = nn.ReLU()
        self.outfunc = nn.Sigmoid()

    def forward(self,x):
        out = self.actfunc(torch.matmul(x,self.w1)+self.b1)
        out = self.actfunc(torch.matmul(out,self.w2)+self.b2)
        out = self.actfunc(torch.matmul(out,self.w3)+self.b3)
        out = self.actfunc(torch.matmul(out,self.w4)+self.b4)
        out = self.actfunc(torch.matmul(out,self.w5)+self.b5)
        out = self.outfunc(torch.matmul(out,self.w6))
        # out = exp(torch.matmul(out,self.w6))
        # print(out)
        return 1/(1+out)

class Netv1(nn.Module):

    def __init__(self):
        super().__init__()
        self.w1 = nn.Parameter(torch.randn(10000, 1000)*exp(2/10000))
        self.b1 = nn.Parameter(torch.zeros(1000))

        self.w2 = nn.Parameter(torch.randn(1000, 1000)*exp(2/1000))
        self.b2 = nn.Parameter(torch.zeros(1000))

        self.w3 = nn.Parameter(torch.randn(1000, 800)*exp(2/1000))
        self.b3 = nn.Parameter(torch.zeros(800))

        self.w4 = nn.Parameter(torch.randn(800, 400)*exp(2/800))
        self.b4 = nn.Parameter(torch.zeros(400))

        self.w5 = nn.Parameter(torch.randn(400, 1)*exp(2/400))
        # self.w5 = nn.Parameter(torch.randn(10000, 2))

    def forward(self, x):
        h1 = nn.functional.relu(x @ self.w1 + self.b1)
        # print(h1)
        h2 = nn.functional.relu(h1 @ self.w2 + self.b2)
        # print(h2)
        h3 = nn.functional.relu(h2 @ self.w3 + self.b3)
        # print(h3)
        h4 = nn.functional.relu(h3 @ self.w4 + self.b4)
        # print(h4)
        h5 = h4 @ self.w5
        # h5 = x @ self.w5


        # 定义softmax
        # h = torch.exp(h5)
        # print(h)
        # z = torch.sum(h, dim=1, keepdim=True)
        # print(z)
        h = torch.nn.functional.softmax(h5,dim=1)
        # h = torch.sigmoid(h5)
        return h


if __name__ == '__main__':
    net = Netv3()
    x = torch.randn(1, 10000)
    y = net(x)
    print(y[0])
    print(y.shape)
