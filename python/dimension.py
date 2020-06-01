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

# ===============================线性代数=====================================
#求行列式：
# a = np.array([[1,2],[3,4]])
# print(np.linalg.det(a))
# #求行列式：
# b = tc.tensor([[1.,2.],[3.,4.]])
# print(b.det())
#
# #对角阵
# c = np.diag([1,2,3,4,5])
# print(c)
# #对角阵
# d = tc.diag(tc.tensor([1,2,3,4,5]))
# print(d)

#单位矩阵
# e = np.eye(3)
# e = np.eye(3,4)
# print(e)

#单位矩阵
# d = tc.eye(3)
# d = tc.eye(3,4)
# print(d)

#下三角矩阵
# e = np.tri(3,3)
# print(e)

# f = tc.tril(tc.ones(3,3))
# print(f)

#1矩阵
# f = np.ones((3,3))
# print(f)
#
# g = tc.ones(3,3)
# print(g)

#0矩阵
# f = np.zeros((3,3))
# print(f)
#
# g = tc.zeros(3,3)
# print(g)

#求内积
# a = np.array([1,2])
# b = np.array([3,4])
# print(np.sum(a*b))

# a = tc.tensor([[1.,2.],[3.,4.]])
# print(tc.eig(a))#求特征值
# print(tc.eig(a,eigenvectors=True))
