import os,torch,numpy,cv2,turtle
from matplotlib import pyplot as plt
from tqdm import tqdm
from PIL import Image
from torch.nn import *
from thop import profile,clever_format
from torchvision import datasets,transforms
from torch.utils.data import DataLoader,Dataset
import torch.backends.mps as mps
# from _PythonProject._01_DigitalRecognition.write_net import Net

# a = torch.tensor([[0., 0., 0., 0., 1., 0., 0., 0., 0., 0.],
#             [1., 0., 0., 0., 0., 0., 0., 0., 0., 0.]])
# b = torch.tensor([[0.0992, 0.0864, 0.1013, 0.1054, 0.0991, 0.1001, 0.1009, 0.1105, 0.0973,
#              0.0997],
#             [0.1001, 0.0892, 0.1025, 0.0997, 0.0970, 0.0994, 0.1068, 0.1089, 0.1009,
#              0.0954]])
# print(torch.argmax(a,dim=1))
# print(mps.is_available())

# model = Net()
# model.load_state_dict(torch.load("/Users/carbenchueng/Desktop/1-Git/Code/_PythonProject/_01_DigitalRecognition/prarm/0.pt"))
#
# input_tc = torch.randn((1,784))
# traced_script_model = torch.jit.trace(model,input_tc)
# traced_script_model.save("mnist.pt")


# train_data_set = datasets.CIFAR10(root="/Users/carbenchueng/Desktop/2-Data/CIFA10",
#                                   train=True,download=False,transform=transforms.ToTensor())
# test_data_set = datasets.CIFAR10(root="/Users/carbenchueng/Desktop/2-Data/CIFA10",
#                                  train=False,download=False,transform=transforms.ToTensor())
# train_data_loader = DataLoader(train_data_set,batch_size=1000,shuffle=True)
# test_data_loader = DataLoader(test_data_set,batch_size=1000,shuffle=True)

# print(train_data.classes)
# print(type(train_data_set.data[0]))
# print(type(train_data.targets))

# img_data1 = numpy.array(train_data_set.data[0])
# img_data2 = torch.Tensor(train_data_set.data[0])
# # img_data2 =
# print(type(img_data1.shape),type(img_data2.shape))
# print(img_data1.shape,img_data2.shape)

# uncode = transforms.ToPILImage()
# img = uncode(img_data2)
# img.show()


# class Net(Module):
#     def __init__(self):
#         super(Net, self).__init__()
#         self.layers = Sequential(
#             Conv2d(3,16,3,1),
#             LeakyReLU()
#         )
#
#     def forward(self,x):
#         return self.layers(x)
#
# net = Net()
# x = torch.randn(1,3,16,16)
# adap_max = AdaptiveMaxPool2d((1,3))
# y = adap_max(x)
# print(y.shape)
# flops,paraam = profile(net,(x,))
# flops, paraam = clever_format([flops, paraam], "%.3f")
# print(flops)
# print(paraam)


# img1 = cv2.imread("/Users/carbenchueng/Desktop/1-Git/Code/_Image/1.jpg")
# img2 = Image.open("/Users/carbenchueng/Desktop/1-Git/Code/_Image/1.jpg")
# img1 = torch.tensor(img1)
# # print(img1.shape)
# img1 = img1.permute(2,0,1)
# print(img1.dtype,type(img2))


# inn = torch.randn(1,1,5,5)
# conv = Conv2d(1,1,3,1,dilation=1)
# out = conv(inn)
# print(out)


# name = os.listdir(os.chdir("./_PythonProject/_04_YellowPerson/风景"))
# # # print(os.getcwd())
# #
# i = 0
# for old_name in tqdm(name):
#     # print(old_name)
#     os.rename(name[i],f"{str(i)}.jpg")
#     i+=1

#画图
# turtle.color("blue")
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)

img = cv2.imread("/Users/carbenchueng/Desktop/1-Git/Code/_Image/1.jpg")
# img.show()
print(img)






