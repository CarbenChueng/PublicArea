import os,torch,numpy,cv2
from torch.utils.data import Dataset,DataLoader
from PIL import Image,ImageDraw
from torchvision.transforms import *



class YelloKidsDataSet(Dataset):

    def __init__(self,path):
        self.path = path
        self.data_set = os.listdir(self.path)


    def __len__(self):
        return len(self.data_set)
        # pass

    def __getitem__(self, index):
        label = torch.Tensor(numpy.array(self.data_set[index].split(".")[1:5],dtype = numpy.float32)/300)
        img_path = os.path.join(self.path,self.data_set[index])
        img_data = Image.open(img_path)
        img_data = torch.Tensor(numpy.array(img_data))

        # img_data = ToTensor()(img)
        img_data = img_data/255

        return img_data,label


if __name__ == '__main__':
    yd = YelloKidsDataSet("/Users/carbenchueng/Desktop/2-Data/Yellow_Pic/tags")
    data_load = DataLoader(yd,batch_size=1,shuffle=False)
    for i,(img,label) in enumerate(data_load):
        # print(img.shape,label.shape)
        img = img[0].numpy()
        y = label[0].numpy()*300
        img_data = numpy.array(img*255,dtype=numpy.uint8)
        # print(img_data)
        img = Image.fromarray(img_data,"RGB")
        draw = ImageDraw.Draw(img)
        draw.rectangle(y,outline="red",width=2)
        img.show()
        exit()




