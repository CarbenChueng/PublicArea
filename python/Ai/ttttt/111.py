from torchvision import datasets
import torch,numpy

# a = torch.rand(2,3)
# print(a)
# c = torch.zeros(2,3)
# print(c)
# b = torch.tensor([1,2,3,4])

# f = torch.Tensor([1,2,3])
# e = f.new_ones(2,3,dtype=torch.double)
# print(e+a)

# a = torch.Tensor([3.3])
# x = torch.randn(3,2)
# y = x.view(1,-1)
# print(a.item())
# print(y)
# print(y.transpose(1,0))

# n,d_in,h,d_out = 66,1000,100,10
# 
# x = torch.randn(n,d_in)
# # print(x)
# y = torch.randn(n,d_out)
# 
# w1 = torch.randn(d_in,h)
# w2 = torch.randn(h,d_out)
# 
# leartning_rate = 1e-6
# for it in range(100):
#     h = x.mm(w1)
#     h_relu = h.clamp(min=0)
#     y_pred = h_relu.mm(w2)
#     
#     lloss = (y-y_pred).pow(2).sum().item()
#     print(it,lloss)
# 
#     gy_pred = 2.0*(y_pred-y)
#     gw2 = h_relu.t().mm(gy_pred)
#     gh_relu = gy_pred.mm(w2.t())
#     gh = gh_relu.clone()
#     gh[h<0] =0
#     gw1 = x.t().mm(gh)


# def fizz_buzz_encode(i):
#     if i % 15 ==0: return 3
#     elif  i % 5 ==0: return 2
#     elif  i % 3 ==0: return 1
#     else:return 0
# 
# def fizz_buzz_decode(i,predicition):
#     return [str(i),"fizz","buzz","fizzbuzz"][predicition]
# 
# def helper(i):
#     print(fizz_buzz_decode(i,fizz_buzz_encode(i)))
#     
# for i in range(1,20):
#     helper(i)


NUM = 10
def bbb(i,num_digi):
    return numpy.array([i >> d & 1 for d in range(num_digi)])

bbb(15,NUM)