# import numpy as np
#
# num_classes = 10
#
# arr = [1,3,4,5]
# one_hots = np.eye(num_classes)[arr]
# print(one_hots)
#
# tag = [np.argmax(one_hot) for one_hot in one_hots]
# print(tag)

import torch

num_classes = 10
y = torch.tensor([1,2,3,4,5])

one_hot = torch.zeros(y.size(0),num_classes).scatter_(1,y.reshape(-1,1),1)
print(one_hot)
print(one_hot.shape)
