import cv2 as cv
import numpy as np


#=============================================================================
# kkk = cv.imread("a.jpg")

# cv.imshow("out",kkk)
# cv.waitKey(0)

# kkk = cv.VideoCapture(1)
# kkk.set(3,1280)
# kkk.set(4,980)
# kkk.set(10,100)
#
# while True:
#     secc,img = kkk.read()
#     cv.imshow("v",img)
#     if cv.waitKey(1)& 0xFF == ord("q"):
#         break



#==================================================================
# img = cv.imread("a.jpg")
# ker = np.ones((5,5),np.uint8)
#
# imgGray = cv.cvtColor(img,cv.COLOR_BGR2GRAY) #转色
# imgBlur = cv.GaussianBlur(img,(11,11),0) #模糊
# imgCan2 = cv.Canny(imgGray,50,50) #取细节
# imgDia = cv.dilate(imgCan2,ker,iterations=1) #膨胀
# imgEro = cv.erode(imgDia,ker,iterations=1) #腐蚀
#
# cv.imshow("out",imgDia)
# cv.imshow("o",imgCan2)
# cv.imshow("ou",imgEro)
# cv.waitKey(0)


#==================================================================

# img = cv.imread("lambo.jpg")
# w,h,c = img.shape
# img = cv.resize(img,(h//2,w//2),c)
# imgrez = img[0:200,200:800]
# print(imgrez.shape)
# imgGray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# imgCan = cv.Canny(imgGray,60,60)
#
#
# cv.imshow("oq",img)
# cv.imshow("ou",imgrez)
# cv.waitKey(0)


#==================================================================

# img = cv.imread("lambo.jpg")
pt = np.zeros((300,512,3),np.uint8)
# pt[0:100] = 160,0,0
# pt[100:200] = 0,166,0
# pt[200:300] = 0,0,160
cv.line()

print(pt)

# cv.imshow("oq",img)
cv.imshow("ou",pt)
cv.waitKey(0)