import cv2
import numpy as np
from PIL import Image

#=====================================看图===========================================
# 读取图片
# img = cv2.imread("Image/handsome.jpg",0)#代表灰度图
# img = Image.fromarray(img)#因为经过cv2，所以图片颜色有问题opencv变成bgr
# img = img[...,::-1]#变回rgb
# cv2.imshow("pic show",img)#使用opencv自带的窗口显示图片，是个非阻塞方法 “窗口名字”,需要展示的内容
# cv2.waitKey(0)#0是死循环，里面单位是毫秒
# cv2.destroyAllWindows()#摧毁所有窗口


#=====================================画图===========================================
# img = np.random.randint(0,255,(200,300,3),np.uint8)
# img = np.zeros((200,300,3),np.uint8)
# img[:,:,2] = 255
# img[...,2] = 255
# cv2.imwrite("img_save.jpg",img)


#=====================================视频，摄像头===========================================

# cap = cv2.VideoCapture("http://ivi.bupt.edu.cn/hls/cctv1hd.m3u8")#可以读取视频，网络视频（视频格式有要求），数字0不带引号表示摄像头
# # cap = cv2.VideoCapture(0)#0：前置摄像头，1：后置摄像头
# while True:
#     ret,frame = cap.read()#ret返回bool值，判断是否读取成功，frame就是读取到的每一帧画面
#     cv2.imshow("frame",frame)
#     if cv2.waitKey(41) & 0XFF == ord("q"):
#         break
#
# cap.release()#释放视频资源
# cv2.destroyAllWindows()#关闭窗口


#=====================================色彩转换===========================================

src = cv2.imread("../Image/paint.jpg")
dst = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)
ppp = cv2.cvtColor(src,cv2.COLOR_BGR2RGB)
img = Image.fromarray(ppp,"RGB")
img.show()

cv2.imshow("src show",src)
cv2.imshow("dst show",dst)
cv2.waitKey(0)



