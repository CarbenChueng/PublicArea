import numpy as np
import torch as tc
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

# ===============================torch框架=====================================
xb = tc.arange(0, 1, 0.01)
yb = 3 * xb + 2 + tc.rand(100)


class Nai(tc.nn.Module):
    def __init__(self):
        super().__init__()
        self.w = tc.nn.Parameter(tc.rand(1))
        self.b = tc.nn.Parameter(tc.rand(1))

    def forward(self, xx):
        return self.w * xx + self.b


if __name__ == '__main__':
    n = Nai()
    #定义优化器
    opt = tc.optim.SGD(n.parameters(), lr=0.1, momentum=0.1)

    ion = plt.ion()
    for s in range(30):
        for x, y in zip(xb, yb):
            z = n(x)
            looo = (z - y)**2

            opt.zero_grad()

            looo.backward()

            opt.step()
            print(n.w.item(),n.b.item(),looo.item())

        plt.cla()
        plt.plot(xb, yb, ".")
        l = [n.w * i + n.b for i in xb]
        plt.plot(xb, l)

        plt.pause(0.1)
    plt.ioff()
    plt.show()
