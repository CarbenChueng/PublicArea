import numpy as np
import torch as tc

#广播:
a = np.arange(8)
b = np.array([11,12,13,14,15,16,17,18])
c = np.arange(3).reshape(3,1)


# print(a)
# print(b)
# print(c)
# print(a+c)
# print(a+b)


# # print(y[[0,1]])# ==y[:2]
# print(y[[0,1],[0,1]])
# print(y[[0,1,2],[1,0,0]])
# # print(y[[0,1]][:1,[0,1]])
f = np.array([[1, 2,6,3], [3, 3,2,1], [5, 6,1,2]])
u, s, v = np.linalg.svd(f)
print(u, s, v, sep="\n")

d = np.array([[1, 2], [3, 3], [5, 6]])
u, s, v = np.linalg.svd(d)
print(u, s, v, sep="\n")
