import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


#========================================================
#取轮廓
# src = cv.imread("../Image/pic1.jpg")
# kernel = np.array([[1,1,0],[1,0,-1],[0,-1,-1]],np.float32)
# ds = cv.filter2D(src,-1,kernel=kernel)#图片，图片深度，核。-1代表全部拿过来
#
# cv.imshow("show1",src)
# cv.imshow("show2",ds)
# cv.waitKey(0)


#========================================================
#
# src = cv.imread("../Image/pic1.jpg")
#均值滤波（平滑算子）：低通滤波 模糊作用
# ds = cv.blur(src,(5,5))#对传入的图片有要求the depth should be CV_8U, CV_16U, CV_16S, CV_32F or CV_64F.
#高斯滤波：低通滤波，模糊作用
# ds = cv.GaussianBlur(src,(7,7),6)#3,3是核的窗口的大小，1是方差

# cv.imshow("show1",src)
# cv.imshow("show2",ds)
# cv.waitKey(0)


#========================================================
# src = cv.imread("../Image/5.jpg")
# # 中值滤波，处理椒盐噪声
# ds = cv.medianBlur(src,5)#必须是一个大于1的奇数
# 
# 
# cv.imshow("show1",src)
# cv.imshow("show2",ds)
# cv.waitKey(0)


#========================================================
# 双边滤波：保持边缘，降噪平滑，把断断续续的连上
# src = cv.imread("../Image/25.jpg")
# ds = cv.bilateralFilter(src,9,75,75)#图片，领域直径（把握连线的范围），高斯函数标准差，灰度相似度的标准差
#
# cv.imshow("show1",src)
# cv.imshow("show2",ds)
# cv.waitKey(0)


#========================================================

# src = cv.imread("../Image/pic1.jpg")
# 锐化算子，高通滤波，提取轮廓
# kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]],np.float32)
# ds = cv.filter2D(src,-1,kernel=kernel)#图片，图片深度，核。-1代表全部拿过来

# USM锐化
# gs = cv.GaussianBlur(src,(5,5),1)#去燥
# ds = cv.addWeighted(src,2,gs,-1,0)#原图，放大2被，模糊图片，-1倍

# cv.imshow("show1",src)
# cv.imshow("show2",ds)
# cv.waitKey(0)


#========================================================
# 梯度算子（高通滤波）Scharr  Soble
# img = cv.imread("../Image/2.jpg",0)
# laplacian = cv.Laplacian(img,cv.CV_64F)
# # 索贝尔：sobel
# # sobx = cv.Sobel(img,-1,1,0,ksize=5)
# # soby = cv.Sobel(img,-1,0,1,ksize=5)
#
# # scharr
# sobx = cv.Scharr(img,-1,1,0)
# soby = cv.Scharr(img,-1,0,1)
#
# plt.subplot(2,2,1),plt.imshow(img,cmap="gray")
# plt.title("Original"),plt.xticks([]),plt.yticks([])
#
# plt.subplot(2,2,2),plt.imshow(laplacian,cmap="gray")
# plt.title("Laplacian"),plt.xticks([]),plt.yticks([])
#
# plt.subplot(2,2,3),plt.imshow(sobx,cmap="gray")
# plt.title("Sobel x"),plt.xticks([]),plt.yticks([])
#
# plt.subplot(2,2,4),plt.imshow(soby,cmap="gray")
# plt.title("Sobel y"),plt.xticks([]),plt.yticks([])
#
# plt.show()


#========================================================
# canny 边缘提取算法
# img = cv.imread("../Image/1.jpg")
# img = cv.GaussianBlur(img,(3,3),0)
# ds = cv.Canny(img,50,150)
#
#
# cv.imshow("show1",img)
# cv.imshow("show2",ds)
# cv.waitKey(0)


#========================================================

img = cv.imread("../Image/25.jpg")
cv.imshow("or",img)
kenkel = cv.getStructuringElement(cv.MORPH_RECT,(3,3))
img = cv.morphologyEx(img,cv.MORPH_CLOSE,kenkel)

img = cv.convertScaleAbs(img,alpha=6,beta=0)#调整图片对比度，高亮处理
cv.imshow("abs",img)

img = cv.GaussianBlur(img,(5,5),1)
canny = cv.Canny(img,100,150)
canny = cv.resize(canny,dsize=(500,500))
cv.imshow("canny",canny)

cv.waitKey(0)






