import torch

# a = torch.Tensor([[1,2,2,2],[3,4,3,3],[5,6,7,7]])
# print(a.shape)
#
# print(torch.sum(a,dim=1,keepdim=True))
# print(a.numpy())
#
# b = torch.Tensor([[4]])
# print(b.item())

# a = torch.Tensor([[1,3]])
# b = torch.Tensor([[3,3]])
# print(torch.eq(a,b).float())
print(torch.cuda.is_available())