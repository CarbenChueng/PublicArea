import numpy as np
import torch as tc
import torch.nn.functional as f
import matplotlib.pyplot as plt
from PIL import Image

# a=np.array([[1,2,3],[4,5,6]])
# b=tc.tensor([[[12,3,6],[2,8,9]],[[12,3,6],[2,8,9]]])
# print(a.shape)
# print(b)
# print(b.shape)

# ===============================图片查看=====================================

# img = Image.open("a.jpg")
#
# # r,g,b = img.split()#切层
# xs = np.array(img)#转成信息（H,W,C）高，宽，通道
# print(xs.shape)#查看形状
#
# # img.show()
# plt.imshow(img)
# plt.show()


# ===============================矩阵运算=====================================
# a = tc.Tensor([[1,2],[1,2],[1,2]]) #大写的是float
# a = tc.tensor([[3,6],[2,5],[1,7]]) #大写的是float
# b = tc.tensor([[3,6],[3,6],[3,6]]) #小写的是int
# c = tc.tensor([[2,5],[3,4]])
# print(a.shape,b.shape,sep="\n")
# print(a+b)
# print(5+a)
# print(a@c)  #叉乘（不推荐）
# print(tc.matmul(a,c))     #叉乘（推荐）

# print(a.shape)
# print(a.t().shape) #转置


# ===============================张量运算=====================================
# a = tc.tensor([[[3,6,1],[3,6,2]],[[3,6,3],[2,1,2]]])
# b = tc.tensor([[[3,6,1],[3,6,2]],[[3,6,3],[2,1,2]]])
# c = tc.tensor([[[3],[2],[5]],[[3],[6],[2]]])
# print(a,c,sep="\n")
# print(tc.matmul(a,c))

# a = tc.tensor([1,2,3,4,5,6])
# # print(a.reshape(3,2,1))
# b = a.reshape(3,1,2)
# print(b)
# print(b.reshape(6))           #reshape()自定义张量，改变数据纬度


# ===============================numpy的换轴=====================================
# img = Image.open("a.jpg")
# img_data = np.array(img)
# # print(img_data)
# # print(img_data.shape)
#
# #
# k = img_data.reshape(640*640*3)
#
# # print(k.shape)
# k = k.reshape(640,640,3)
# #转置
# f = k.transpose(1,0,2)#换轴
#
# r = Image.fromarray(f)
# r.show()


# ===============================torch的换轴=====================================
# a = tc.rand(1,4,5,3)
# print(a.shape)
# b = a.permute((0,3,2,1))  #换轴
# print(b.shape)


# ===============================逆=====================================
# a = tc.tensor([[1.,2.],[3.,4.]])
# print(tc.inverse(a))
#
# b = np.array([[1.,2.],[3.,4.]])
# print(np.linalg.inv(b))


# ===============================torch框架=====================================
# xb = tc.arange(0, 1, 0.01)
# yb = 3 * xb + 2 + tc.rand(100)
#
#
# class Nai(tc.nn.Module):
#     def __init__(self):
#         super().__init__()
#         self.w = tc.nn.Parameter(tc.rand(1))
#         self.b = tc.nn.Parameter(tc.rand(1))
#
#     def forward(self, xx):
#         return self.w * xx + self.b
#
#
# if __name__ == '__main__':
#     n = Nai()
#     #定义优化器
#     opt = tc.optim.SGD(n.parameters(), lr=0.1, momentum=0.1)
#
#     ion = plt.ion()
#     for s in range(30):
#         for x, y in zip(xb, yb):
#             z = n(x)
#             looo = (z - y)**2
#
#             opt.zero_grad()
#
#             looo.backward()
#
#             opt.step()
#             print(n.w.item(),n.b.item(),looo.item())
#
#         plt.cla()
#         plt.plot(xb, yb, ".")
#         l = [n.w * i + n.b for i in xb]
#         plt.plot(xb, l)
#
#         plt.pause(0.1)
#     plt.ioff()
#     plt.show()


# ===============================全链接非线性拟合=====================================
x = tc.unsqueeze(tc.arange(-10, 10), dim=1)  # unsqueeze升纬,[20,1];[20表示数据的批次，1表示数据的形状]
# print(x)
y = x.pow(3)  # pow定义多少次方


# plt.plot(x,y,".") #plot可以自定义画图符号
# plt.scatter(x, y)  # scatter专门画点
# plt.show()
class Net(tc.nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.w1 = tc.nn.Parameter(tc.randn(1, 30))  # rand 取[2-1)的一组随机数，均匀分布，返回一个张量
        self.b1 = tc.nn.Parameter(tc.zeros(30))  # randn 取(2-1)的一组随机数，标准正态分布，返回一个张量

        self.w2 = tc.nn.Parameter(tc.randn(30, 50))  # rand 取[2-1)的一组随机数，均匀分布，返回一个张量
        self.b2 = tc.nn.Parameter(tc.zeros(50))  # randn 取(2-1)的一组随机数，标准正态分布，返回一个张量

        self.w3 = tc.nn.Parameter(tc.randn(50, 100))  # rand 取[2-1)的一组随机数，均匀分布，返回一个张量
        self.b3 = tc.nn.Parameter(tc.zeros(100))  # randn 取(2-1)的一组随机数，标准正态分布，返回一个张量

        self.w4 = tc.nn.Parameter(tc.randn(100, 50))  # rand 取[2-1)的一组随机数，均匀分布，返回一个张量
        self.b4 = tc.nn.Parameter(tc.zeros(50))  # randn 取(2-1)的一组随机数，标准正态分布，返回一个张量

        self.w5 = tc.nn.Parameter(tc.randn(50, 1))  # rand 取[2-1)的一组随机数，均匀分布，返回一个张量
        self.b5 = tc.nn.Parameter(tc.zeros(1))  # randn 取(2-1)的一组随机数，标准正态分布，返回一个张量

    def forward(self, x):
        fc1 = f.relu(tc.matmul(x, self.w1) + self.b1)
        fc2 = f.relu(tc.matmul(fc1, self.w2) + self.b2)
        fc3 = f.relu(tc.matmul(fc2, self.w3) + self.b3)
        fc4 = f.relu(tc.matmul(fc3, self.w4) + self.b4)
        fc5 = tc.matmul(fc4, self.w5) + self.b5

        return fc5


if __name__ == '__main__':
    net = Net()
    optim = tc.optim.Adam(net.parameters(),lr=0.1)
    loss_func = tc.nn.MSELoss()  # 均方差
    plt.ion()
    for i in range(1000):
        out = net(x.float())
        loss = loss_func(out, y.float())

        optim.zero_grad()  # 清空梯度
        loss.backward()  # 求导
        optim.step()  # 更新参数

        if i % 5 == 0:
            plt.cla()
            plt.scatter(x, y)
            plt.plot(x, out.detach().numpy(), "r")
            plt.pause(0.1)

        plt.show()
