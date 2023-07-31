import torch,os

b = open("new.txt")
# print(b)

for i,s in enumerate(b):
    s = s.strip().split()
    print(s)

# a = torch.rand(12,6)
# print(a)
# print(torch.gt(a, 0.5))
# idxs = torch.nonzero(torch.gt(a, 0.5))
# for idx in idxs:
#     print(a[idx[0],idx[1]])