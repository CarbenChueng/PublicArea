import numpy as np

#广播:
a = np.arange(12).reshape(3,4)
b = np.arange(4)
c = np.arange(3).reshape(3,1)

# print(a+b)
print(c)
print(a+c)



a = np.array([[1, 2], [3, 3], [5, 6]])
u, s, v = np.linalg.svd(a)
# print(u, s, v, sep="\n")
