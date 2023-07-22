import matplotlib.pyplot as plt
from PIL import Image
import os
import torch
import numpy
import cv2

# print(torch.backends.mps.is_available())
# print(torch.version)
# device = torch.device("mps")
# x = torch.randn(128,128,device=device)
# net = torchvision.models.resnet18().to(device)
# print(x.device)
# print(next(net.parameters()).device)


# =================================作业==============================
# 利用matplotlib把每张图片依次展示，暂停一秒


# path = os.listdir("../Image")
#
# for i in path:
#     plt.ion()
#     img = Image.open("Image/%s" % i)
#     plt.imshow(img)
#     plt.show()
#     plt.pause(1)
#
# plt.ioff()

# x = numpy.arange(-10,11)

# y = numpy.tile(numpy.array(3),x.shape)
# y1 = x**2
# y2 = x**3
# y3 = numpy.log(x)
# y4 = numpy.log(x)/numpy.log(numpy.array(0.5))



# plt.plot(numpy.zeros_like(x))
# plt.plot((x,y1),(x,y2))
# plt.plot(x,y1,x,y2)
# plt.plot(x,y4)

# plt.show()
# print(x)

# img = torch.empty((200,200,3))
# img = img.numpy()
# cv2.imwrite("233.jpg",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# =================================测试==============================
img = cv2.imread("../../Image/girl.jpg")
w,h,c = img.shape
kkk = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
ds = cv2.resize(img,(h//2,w//2),interpolation=cv2.INTER_CUBIC)
# ds = cv2.morphologyEx(img1,cv2.MORPH_GRADIENT,kernel)
girl = cv2.morphologyEx(ds,cv2.MORPH_GRADIENT,kkk)


cv2.imshow("g",girl)
cv2.waitKey(0)
cv2.destroyAllWindows()