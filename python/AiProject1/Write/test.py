import numpy as np,torch,os,torch.nn as nn
from PIL import Image,ImageDraw
from AiProject1.YellowPerson.img_data import dataset
from AiProject1.YellowPerson.net import cnn_net
from torch.utils import data


# print(torch.cuda.is_available())
# print(torch.__version__)



a = np.array((1,2,3))
img = Image.fromarray(a,"RGB")

img.show()


