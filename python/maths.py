import torch

import random
import numpy as np
import matplotlib.pyplot as plt

# ====================================================================
# a = torch.tensor(3)
# c = torch.tensor([[1,2,3],[4,5,6]])#二维张量
# print(a,c)

# b = np.array(2)
# print(b)

# f= a.numpy()#转换成numpy
# print(type(f))

# e = torch.from_numpy(b)#转换成torch
# print(type(e))


# ===============================指数函数=====================================
# x = np.arange(-10,10,1.)#指数函数框架问题。要带小数点
# print(x.shape)
# y = 2**x
# y1 = np.tile(np.array([3]),x.shape)
#
# # print(x)
# plt.plot(x,y)
# # plt.plot(x,y1)
# print(plt.show())


# ===============================对数函数=====================================
# y = loga**x

# x = np.arange(0.2,10,0.1)
#
# y= np.log(x)
# y2= np.zeros_like(x)
# y3 = np.log(x)/np.log(np.array([0.5]))
#
# plt.plot(x,y)
# plt.plot(x,y2)
# plt.plot(x,y3)
# print(plt.show())


# ===============================对数函数=====================================
# tanh(z) = e**z - e**(-z)/e**z + e**(-z)
# t = np.arange(-10,10,0.1)
# r = (np.exp(t)-np.exp(-t))/(np.exp(t)+np.exp(-t))
# 
# plt.plot(t,r)
# 
# 
# # sigmoid(z) = 1/1+e**(-z)
# x = np.arange(-10,10,0.1)
# y = 1/(1+np.exp(-x))
# 
# plt.plot(x,y)
# print(plt.show())

# ===============================求导=====================================
# x = torch.tensor([3.0],requires_grad=True)
# y = x**3+2
# 第一种
# y.backward()
# print(x.grad)

# 第二种（少用）
# print(torch.autograd.grad(y,x))


# ===============================梯度下降，例子=====================================
# 随机生成点X
# _x = [i / 100 for i in range(100)]
# # 创建方程式，为了分散点的轨迹加上random随机数（random.random()是增加0-1之间的其中一个值）
# _y = [3 * e + 5 + random.random() for e in _x]
#
# w = random.random()
# b = random.random()
#
# plt.ion()#开启会话
#
# # 训练30次
# for i in range(30):
#     for x, y in zip(_x, _y):
#         z = w * x + b
#
#         o = z - y
#         loss = o ** 2
#
#         dw = -2 * o * x
#         db = -2 * o
#
#         w = w + 0.1 * dw
#         b = b + 0.1 * db
#         print(w, b, loss)
#     v = [w * e + b for e in _x]
#     plt.cla()#清屏
#     plt.plot(_x, _y, "*")
#     plt.plot(_x, v)
#     plt.title(loss)#显示损失
#     plt.pause(0.01)
#
# plt.ioff()#结束会话
# plt.show()#停顿


# ===============================torch框架=====================================

xs = torch.arange(0, 1, 0.01)
ys = 8 * xs + 2 + torch.rand(100)  # 取0-1


# plt.plot(xs,ys,"^")
# plt.show()
class Line(torch.nn.Module):
    def __init__(self):  # 初始化
        super().__init__()
        # 初始化模型
        self.w = torch.nn.Parameter(torch.rand(1))  # 构建系统参数，自动优化,参数值是随机的
        self.b = torch.nn.Parameter(torch.rand(1))  # 构建系统参数，自动优化,参数值是随机的

    def forward(self, x):
        return self.w * x + self.b


if __name__ == "__main__":
    line = Line()
    # 定义优化器
    opt = torch.optim.SGD(line.parameters(), lr=0.1,momentum = 0.1)
    #他根据梯度对步长的自动更改
    # opt = torch.optim.Adam(line.parameters(),lr=0.1)
    
    # 定义损失函数
    # loss = torch.nn.MSELoss()
    ion = plt.ion()
    for epoch in range(30):
        for x, y in zip(xs, ys):
            z = line(x)
            loss = (z-y)**2
            #梯度清空
            opt.zero_grad()
            #自动求导
            loss.backward()
            #参数更新
            opt.step()
            print(line.w.item(),line.b.item(),loss.item())
        plt.cla()
        plt.plot(xs,ys,"^")
        v = [line.w*r+line.b for r in xs]
        plt.plot(xs,v)

        plt.pause(0.01)
    plt.ioff()
    plt.show()