import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


#========================================================
#取轮廓
# src = cv.imread("../Image/pic1.jpg")
# kernel = np.array([[1,1,0],[1,0,-1],[0,-1,-1]],np.float32)
# # kernel = np.float32([[1,1,0],[1,0,-1],[0,-1,-1]])
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
img = cv.imread("../../Image/1.jpg")
img = cv.GaussianBlur(img,(3,3),0)
ds = cv.Canny(img,50,150)


cv.imshow("show1",img)
cv.imshow("show2",ds)
cv.waitKey(0)


#========================================================

# img = cv.imread("../Image/25.jpg")
# cv.imshow("or",img)
# kenkel = cv.getStructuringElement(cv.MORPH_RECT,(3,3))
# img = cv.morphologyEx(img,cv.MORPH_CLOSE,kenkel)
#
# img = cv.convertScaleAbs(img,alpha=6,beta=0)#调整图片对比度，高亮处理
# cv.imshow("abs",img)
#
# img = cv.GaussianBlur(img,(5,5),1)
# canny = cv.Canny(img,100,150)
# canny = cv.resize(canny,dsize=(500,500))
# cv.imshow("canny",canny)
#
# cv.waitKey(0)


#========================================================
# 轮廓描绘
# img = cv.imread("../Image/26.jpg")
# img_gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# #二值化
# ret,thresh = cv.threshold(img_gray,127,255,0)
# #找轮廓       列表形式返回轮廓数量，    =  （值，表示轮廓，提取轮廓方式）
# #findContours包含canny
# contours,_ = cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
# print(contours,_)
# img_con = cv.drawContours(img,contours,-1,(255,0,0),2)
#
# cv.imshow("canny",img_con)
#
# cv.waitKey(0)


#========================================================
# 计算轮廓
# img = cv.imread("../Image/14.jpg",0)
#
# ret,thresh = cv.threshold(img,127,255,0)
# contours,_ = cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
#
# m = cv.moments(contours[0])#矩
# cx,cy = int(m["m10"]/m["m00"]),int(m["m10"]/m["m00"])
# print("重心：",cx,cy)#重心就是质心，每个像素单位为1个重量，求出重量的中心点
#
# area = cv.contourArea(contours[0])#面积就是像素的个数
# print("面积：",area)
#
# perimter = cv.arcLength(contours[0],True)
# print("面积：",perimter)


#========================================================
# 轮廓近似
# img = cv.imread("../Image/26.jpg")
# img_g = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#
# ret,thresh = cv.threshold(img_g,127,255,0)
#
# contours,_ = cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
#
# epsilon = 40 #值越大，简化效果越厉害
# approx = cv.approxPolyDP(contours[0],epsilon,True)
#
# img_con = cv.drawContours(img,[approx],-1,(0,255,0),3)
#
# cv.imshow("a",img_con)
# cv.waitKey(0)


#========================================================
# 凸包，凸性检测
# img = cv.imread("../Image/16.jpg")
# img_g = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#
# ret,thresh = cv.threshold(img_g,127,255,0)
#
# contours,_ = cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
#
# hull = cv.convexHull(contours[0])
# print(cv.isContourConvex(contours[0]),cv.isContourConvex(hull))
#
# img_con = cv.drawContours(img,[hull],-1,(0,255,0),3)
#
# cv.imshow("a",img_con)
# cv.waitKey(0)


#========================================================
# 边界检测,切图，得到形状方向
# img = cv.imread("../Image/16.jpg")
# img_g = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#
# ret,thresh = cv.threshold(img_g,127,255,0)
#
# contours,_ = cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
# #拿到边界矩形
# x,y,w,h = cv.boundingRect(contours[0])
#
# img_con = cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)
# #最小矩形
# rect = cv.minAreaRect(contours[0])
# box = cv.boxPoints(rect)
# box = np.int0(box)
# img_c = cv.drawContours(img,[box],0,(0,0,255),3)
# #最小外切圆
# (x,y),radius = cv.minEnclosingCircle(contours[0])
# center = (int(x),int(y))
# radius = int(radius)
# img_co = cv.circle(img,center,radius,(0,255,0),3)
#
#
# cv.imshow("a",img_con)
# cv.waitKey(0)


#========================================================
# 边界检测,切图，得到形状方向
# img = cv.imread("../Image/16.jpg")
# img_g = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#
# ret,thresh = cv.threshold(img_g,127,255,0)
# contours,_ = cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
#
# ellipse = cv.fitEllipse(contours[0])
# cv.ellipse(img,ellipse,(255,0,0),3)
#
# h,w,_ = img.shape
# [vx,vy,x,y] = cv.fitLine(contours[0],cv.DIST_L2,0,0.01,0.01)
# lefty = int((-x*vy/vx)+y)
# righty = int(((w-x)*vy/vx)+y)
# cv.line(img,(w-1,righty),(0,lefty),(0,0,255),2)
#
# cv.imshow("a",img)
# cv.waitKey(0)


#========================================================
# 霍夫直线
# img = cv.imread("a.jpg")
# imgGray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#
# edges = cv.Canny(imgGray,50,100)
# cv.imshow("canny",edges)
#
# lines = cv.HoughLines(edges,1,np.pi/180,100)
# #图片，步长1（1个像素）度数的步长，预值（精确度）
#
# cv.waitKey(0)


# 霍夫圆
# img = cv.imread("allshape.jpeg")
# imgGray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# edges = cv.Canny(imgGray,50,100)
# circle = cv.HoughCircles(edges,cv.HOUGH_GRADIENT,1,150,param1=40,param2=20,minRadius=20,maxRadius=100)
# #图片，方法，梯度值，最小半径，p1=canny双边预值处理，p2=累加器，最大半径。并且返回x,y,r三个值
#
# for i in circle[0,:]:
#     circle = np.uint16(np.around(circle))
#     cv.circle(img,(i[0],i[1]),i[2],(0,0,255),3)#3是弧长
#
#
# cv.imshow("canny",img)
# cv.waitKey(0)



#========================================================
# 分水岭算法
# img = cv.imread('allshape.jpeg')
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# ret, thresh = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
#
# # noise removal
# kernel = np.ones((3, 3), np.uint8)
# opening = cv.morphologyEx(thresh, cv.MORPH_OPEN, kernel, iterations=2)
#
# # sure background area
# sure_bg = cv.dilate(opening, kernel, iterations=3)
# # sure_bg = opening
#
# dist_transform = cv.distanceTransform(opening, 1, 5)
# ret, sure_fg = cv.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)
#
# cv.imshow("123",opening)
# cv.imshow("1",dist_transform)
# print(dist_transform)
# cv.imshow('2',sure_fg)
# cv.waitKey(0)
#
# # Finding unknown region
# sure_fg = np.uint8(sure_fg)
# unknown = cv.subtract(sure_bg, sure_fg)
# print(unknown.dtype)
# print(sure_fg.dtype)
# # Marker labelling
# ret, markers1 = cv.connectedComponents(sure_fg)
# print(markers1.dtype)
# # Add one to all labels so that sure background is not 0, but 1
# markers = markers1 + 1
# # Now, mark the region of unknown with zero
# markers[unknown == 255] = 0
#
# print(markers)
#
# markers3 = cv.watershed(img, markers)
# img[markers3 == -1] = [0, 0, 255]
#
# cv.imshow("img", img)
# cv.waitKey(0)










