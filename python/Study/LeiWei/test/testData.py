import os,torch
from PIL import Image
from torch.utils.data import Dataset
from torchvision import transforms


class MyDataSet(Dataset):
    def __init__(self,path):
        self.path = path
        self.dataSet = os.listdir(path)

    def __len__(self):
        return len(self.dataSet)

    def __getitem__(self, item):
        name = self.dataSet[item]
        img = Image.open(os.path.join(self.path,name))
        img = transforms.ToTensor()(img)

        target = int(name.split(".")[0])
        target = torch.Tensor([target])

        return img,target


if __name__ == '__main__':
    # print(os.listdir("D:\tag\CDData\CDTest\Cat"))
    data = MyDataSet("D:\data\CDData\CDTest\Cat")
    # print(tag[0].shape)
    print(data[0][1])



