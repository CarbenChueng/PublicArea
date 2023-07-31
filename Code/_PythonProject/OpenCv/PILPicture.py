from PIL import Image, ImageFilter ,ImageDraw,ImageFont# PIL图片操作
import matplotlib.pyplot as plt  # 可以画图和展示图片
import random
import numpy as np
from mpl_toolkits.mplot3d import Axes3D   #导入3d坐标系


# img = Image.open(r"Image/food.jpg")
# img.show() #操作系统查看图片
# plt.imshow(img)
# plt.title("haha")
# plt.show()

# w, h = img.size
# print(w, h)
# print(img.size) #元组形式返回
# bands = img.getbands()#获取通道
# print(bands)
# mode = img.mode
# print(mode)

# 图片缩放
# img = img.resize((100,66))#尺寸缩放图片
# img.show()

# img.thumbnail((w // 2, h // 2),resample = Image.ANTIALIAS)  # 等比缩放图片，原图采样, res****抗锯齿
# img.show()

# 抠图
# img = img.crop((10,10,100,100)) #图片左上角和右下角的坐标

# 旋转
# img = img.rotate(45) #从右到左，
# img = img.rotate(-90) #从右到左，超过180就用负数

# 滤波器
# img = img.filter(ImageFilter.CONTOUR) #素描效果
# img = img.filter(ImageFilter.BLUR) #模糊效果
# img = img.filter(ImageFilter.BoxBlur(radius=0)) #模糊效果,radius模糊程度
# img = img.filter(ImageFilter.DETAIL) #锐化
# img = img.filter(ImageFilter.EMBOSS) #浮雕
# img = img.filter(ImageFilter.EDGE_ENHANCE) #增强纹理


# 加logo
# logo = Image.open("Image/paint.jpg")
# logo = logo.resize((50, 50), resample=Image.ANTIALIAS)
# img.paste(logo,(200,200)) #粘贴，第二个属性是粘贴的位置
#
# plt.imshow(img)
# plt.show()


#==============================================================================


#生成验证码
# class GenerateCode:
#     #生成随机数据
#     def getcode(self): #(65-90)A~Z
#         return chr(random.randint(65,90))
#
#     # 背景颜色1
#     def bg_color(self):
#         return (random.randint(0,160),
#                 random.randint(0,160),
#                 random.randint(0,160))
#
#     # 背景颜色2
#     def fn_color(self):
#         return (random.randint(161,255),
#                 random.randint(161,255),
#                 random.randint(161,255))
#
#     # 验证码
#     def gen_pic(self):
#         # 创建画板
#         w,h = 200,80
#         img = Image.new(size=(w,h),mode="RGB",color=(255,255,255))
#         # 画笔
#         draw = ImageDraw.Draw(img)
#         # 字体
#         font_n = ImageFont.truetype(font="Noteworthy.ttc",size=25)
#
#         for y in range(h):
#             for x in range(w):
#                 draw.point((x,y),fill=self.bg_color())
#
#         for i in range(4):
#             draw.text((55*i+10,20),text=self.getcode(),fill=self.fn_color(),font=font_n)
#             draw.rectangle((5,25,30,60))#画矩形框框
#         # img.save("NFonts.jpg")
#
#
#         plt.imshow(img)
#         plt.show()
#
# g = GenerateCode()
# g.gen_pic()


#===========================================3D画图===================================


# x = np.random.normal(0,1,100) #标准正态分布（均值，方差，采集数量）
# y = np.random.normal(0,1,100) #标准正态分布（均值，方差，采集数量）
# z = np.random.normal(0,1,100) #标准正态分布（均值，方差，采集数量）
#
# fig = plt.figure() #生成坐标系
# ax = Axes3D(fig)
# ax.scatter(x,y,z,c = "purple",marker="1")
# # plt.imshow(ax)
# plt.show()


#===========================================实时画图===================================


# ax = []
# ay = []
#
# plt.ion()
# for i in range(100):
#     ax.append(i)
#     ay.append(i**2)
#
#     # 清除 clf清除当前画板内容，cla清除整个画板
#     plt.clf()
#     plt.plot(ax,ay,c = "pink")#画折线图
#     # plt.scatter(ax,ay) #画点
#
#     plt.pause(0.5)
# plt.ioff()
# plt.show()


#===========================================实时画图===================================


# x = np.random.randn(20)
# y = np.random.randn(20)
#
# # 画点
# plt.scatter(x,y,c = "r",marker="p",s=80,label="car")
# plt.legend()#显示图例
# plt.show()









