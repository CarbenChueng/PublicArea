import os
import torch
from torch.utils import data
from PIL import Image,ImageDraw
import numpy as np

class dataset(data.Dataset):
    def __init__(self,path):
        self.path = path
        self.dataset = []
        self.dataset.extend(os.listdir(path))
    def __len__(self):
        return len(self.dataset)
    def __getitem__(self, index):
        label = torch.Tensor(np.array(self.dataset[index].split(".")[1:5],dtype=np.float32)/300)
        img_path = os.path.join(self.path,self.dataset[index])
        img = Image.open(img_path)
        img_data = torch.Tensor(np.array(img)/255-0.5)
        return img_data,label
if __name__ == '__main__':
    mydata = dataset("D:\PyCharmProject\AiProject1\YellowPerson\img\dtag")
    dataloader = data.DataLoader(dataset=mydata,batch_size=10,shuffle=True)
    for i,(x,y) in enumerate(dataloader):


        print(x.size())
        print(y.size())
        x = x[0].numpy()
        y = y[0].numpy()
        img_data = np.array((x+0.5)*255,dtype=np.int8)
        img = Image.fromarray(img_data,"RGB")
        draw = ImageDraw.Draw(img)
        draw.rectangle(y*300,outline="red",width=2)
        img.show()
