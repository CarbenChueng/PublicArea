import json,random,time,pyautogui
import os, torch, numpy, cv2, turtle
from matplotlib import pyplot as plt
from tqdm import tqdm
from PIL import Image
from torch.nn import *
from thop import profile, clever_format
from torchvision import datasets, transforms
from torch.utils.data import DataLoader, Dataset

# import torch.backends.mps as mps,json

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

# 画图
# turtle.color("blue")
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)

# with open("/Users/carbenchueng/Desktop/1-Git/Code/_Image/1.jpg","rb") as file:
#     lines = file.readlines()
#     with open("/Users/carbenchueng/Desktop/1-Git/Code/_Image/1_bak.jpg","wb") as file_bak:
#         file_bak.writelines(lines)


# d1 = {"name": "carben", "age": 18}
# json_str = json.dumps(d1)  # 转成json
# print(type(json_str), json_str)
# python_str = json.loads(json_str)  # 转成python
# print(type(python_str), python_str)

# data = [
#     ['path', 'x', 'y', 'W', 'h'],
#     ['1.png', '100', '100', '200', '200'],
#     ['2.png', '50', '100', '100', '100'],
#     ['3.png', '200', '50', '150', '100'],
#     ['4.png', '150', '100', '100', '100']
# ]
#
# with open("data.txt","w+",encoding="UTF-8") as f:
#
#     for i in data:
#         for e in i:
#         # print(i)
#             f.write(e +"\t")
#         f.write("\n")
# with open("data.txt","r",encoding="UTF-8") as af:
#     print(af.read())

# boxes = numpy.array([[6, 17, 8, 9], [33,66,55,11],[10, 21, 15, 25]])
# x = numpy.argsort(boxes[:,0])
# new_boxes = boxes[x]
# print(new_boxes[0])

# igg = Image.open("/Users/carbenchueng/Desktop/2-Data/Celeba/sample/012022.jpg")
# print(igg.size)


# img = cv2.imread("/Users/carbenchueng/Desktop/2-Data/Celeba/sample/000477.jpg")
# img = cv2.imread("/Users/carbenchueng/Desktop/2-Data/Celeba/sample/000441.jpg")
# cv2.rectangle(img,(30,56),(93,143),(0,0,255),thickness=3)
# cv2.rectangle(img,(115,152),(213,275),(0,0,255),thickness=3)
# cv2.drawMarker(img,(165,184),(0,0,255),thickness=2)
# cv2.drawMarker(img,(244,176),(0,0,255),thickness=2)
# cv2.drawMarker(img,(196,249),(0,0,255),thickness=2)
# cv2.drawMarker(img,(194,271),(0,0,255),thickness=2)
# cv2.drawMarker(img,(266,260),(0,0,255),thickness=2)
# cv2.imshow("pic",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# 150 130 198 191


# x = torch.randn(1,1,15,15)
# lays = Sequential(
#     Conv2d(1,1,4,1),
#     Conv2d(1,1,4,1),
#     Conv2d(1,1,4,1),
#     Conv2d(1,1,4,1),
#     Conv2d(1,1,3,1),
#     Conv2d(1,1,3,1),
    # Conv2d(1,1,3,1),
    # Conv2d(1,1,3,1),
    # Conv2d(1,1,3,1),
    # Conv2d(1,1,3,1),
# )

# print(lays(x).shape)

# x = torch.tensor((1,2,3,4,5,6))
# print(x[x>=2])
# print(torch.unsqueeze(x,dim=0))


# img = Image.open("/Users/carbenchueng/Desktop/1-Git/Code/_Image/1.jpg")
# print(img.size)
# face_crop = img.crop([100,100,200,200])
# face_resize = face_crop.resize((100, 100), Image.Resampling.LANCZOS)
# face_resize1 = face_crop.resize((100, 100))

#1：读取到两个文件的内容 一条一条的读
#2：把五官的坐标点在label的末端添加

# conv = Conv2d(1,1,7)
#
# class Net(Module):
#     def __init__(self):
#         super(Net, self).__init__()
#         self.layers = Sequential(
#             Conv2d(1,1,3),
#             PReLU(),
#             Conv2d(1,1,3),
#             PReLU(),
#             Conv2d(1,1,3),
#             PReLU(),
#
#         )
#
#     def forward(self,x):
#         return self.layers(x)
#
# net = Net()
# x = torch.randn(1,1,7,7)
# y1 = conv(x)
# y2 = net(x)
# print(y1.shape)
# print(y2.shape)


try:

    with open("/Users/carbenchueng/Desktop/2-Data/Celeba/test_face/48/positive.txt", "r") as positive_anno_file:
        fsss = positive_anno_file.read()
        print(fsss)
    with open("/Users/carbenchueng/Desktop/2-Data/Celeba/test_face/48/negative.txt", "r") as negative_anno_file:
        pass
    with open("/Users/carbenchueng/Desktop/2-Data/Celeba/test_face/48/part.txt", "r") as part_anno_file:
        pass

    # print("-"*50)
    # anno_src =  "/Users/carbenchueng/Desktop/2-Data/Celeba/label_1.txt"
    # img_dir = r"/Users/carbenchueng/Desktop/2-Data/Celeba/sample"
    # for i, line in enumerate(tqdm(open(anno_src))):
    #     strs = line.split()
    #     # print(i,line)
    #     img_file_name = strs[0]
    #
    #     img_file = os.path.join(img_dir, img_file_name)
    #     print(img_file)
    #     with Image.open(img_file) as img:  # 打开图片文件
    #         img_w, img_h = img.size
    #         print(img_w,img_h)
    #         x1 = int(strs[1])
    #         x2 = int(strs[3])
    #         y1 = int(strs[2])
    #         y2 = int(strs[4])
    #         w = x2 - x1
    #         h = y2 - y1
    #         print(w,h)
    #         for _i in range(1):
    #             # side_len = numpy.random.randint(48, min(img_w, img_h) / 2)
    #             side_len = numpy.random.randint(48, min(63, 87) / 2)
    #             # side_len = numpy.random.randint(8, 5)
    #             print(side_len)

except Exception as e:
    print(e)
    ff = open("Erro.txt","a+")
    ff.write(str(e))






