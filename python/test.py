import torch
import random
import numpy as np
import matplotlib.pyplot as plt


#====================================================================
a = torch.tensor(3)
c = torch.tensor([[1,2,3],[4,5,6]])#二维张量
# print(a,c)

b = np.array(2)
# print(b)

f= a.numpy()#转换成numpy
# print(type(f))

e = torch.from_numpy(b)#转换成torch
# print(type(e))


#===============================指数函数=====================================
# x = np.arange(-10,10,1.)#指数函数框架问题。要带小数点
# print(x.shape)
# y = 2**x
# y1 = np.tile(np.array([3]),x.shape)
#
# # print(x)
# plt.plot(x,y)
# # plt.plot(x,y1)
# print(plt.show())


#===============================对数函数=====================================
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


#===============================对数函数=====================================
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

#===============================求导=====================================
# x = torch.tensor([3.0],requires_grad=True)
# y = x**3+2
# 第一种
# y.backward()
# print(x.grad)

# 第二种（少用）
# print(torch.autograd.grad(y,x))


#===============================梯度下降，例子=====================================
_x = [i/100 for i in range(100)]
_y = [3*e+4+random.random() for e in _x]
# print(_x)
# print(_y)

w = random.random()
b = random.random()
for i in range(30):
    for x,y in zip(_x,_y):
        z = w*x+b

        o = z-y
        loss = o**2

        dw = -2*o*x
        db = -2*o

        w = w+0.1*dw
        b = b+0.1*db
        print(w,b,loss)
        
plt.plot(_x,_y,".")
v = [w*e+b for e in _x]
plt.plot(_x,v)
plt.show()





