import matplotlib.pyplot as plt
from PIL import Image
import os



# =================================作业==============================
# 利用matplotlib把每张图片依次展示，暂停一秒


path = os.listdir("../Image")

for i in path:
    plt.ion()
    img = Image.open("Image/%s" % i)
    plt.imshow(img)
    plt.show()
    plt.pause(1)

plt.ioff()
