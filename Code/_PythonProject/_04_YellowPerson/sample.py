import os
from PIL import Image
import numpy as np

bg_path = "/Users/carbenchueng/Desktop/1-Git/Code/_PythonProject/_04_YellowPerson/风景"
x = 1
for filename in os.listdir(bg_path):
    print(filename)
    background = Image.open(f"{bg_path}/{filename}")
    shape = np.shape(background)
    if len(shape) == 3 and shape[0]>100 and shape[1]>100:
        background = background
    else:
        continue
    background_resize = background.resize((300,300))
    # background_resize = background.resize.convert("RGB")

    name = np.random.randint(1,21)
    img_font = Image.open(f"/Users/carbenchueng/Desktop/2-Data/Yellow_Pic/{name}.png")
    ran_w = np.random.randint(50,180)
    img_new = img_font.resize((ran_w,ran_w))

    ran_x1 = np.random.randint(0,300-ran_w)
    ran_y1 = np.random.randint(0,300-ran_w)

    r,g,b,a = img_new.split()
    background_resize.paste(img_new,(ran_x1,ran_y1),mask=a)

    ran_x2 = ran_x1+ran_w
    ran_y2 = ran_y1+ran_w

    background_resize.save("/Users/carbenchueng/Desktop/2-Data/Yellow_Pic/tags/{0}{1}.png".format(x,"."+str(ran_x1)+"."+str(ran_y1)+
                                                    "."+str(ran_x2)+"."+str(ran_y2)))
    x+=1