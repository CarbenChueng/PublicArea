import torch,os,numpy as np
from PIL import Image
from torch.utils.data import Dataset

class FaceDataset(Dataset):
    def __init__(self,path):
        self.path = path
        self.dataset = []
        self.dataset.extend(open(os.path.join(path,"positive.txt")).readlines())
        self.dataset.extend(open(os.path.join(path,"negative.txt")).readlines())
        self.dataset.extend(open(os.path.join(path,"part.txt")).readlines())
        # print(self.path)

    def __len__(self):
        return len(self.dataset)

    def __getitem__(self, item):
        # strs1 = self.dataset[item].strip().split()
        strs = self.dataset[item].split()

        cond = torch.Tensor([int(strs[1])])
        offset = torch.Tensor([float(strs[2]),float(strs[3]),float(strs[4]),float(strs[5])])
        print(offset)

        # img_path = os.path.join(self.path,strs[0])
        # img = Image.open(img_path)
        # print((torch.Tensor(np.array(img))/255.-0.5).shape)
        # img.show()
        # img_data = torch.Tensor(np.array(Image.open(img_path))/255. - 0.5)
        # img_data = img_data.permute(2,0,1)
        # return img_data,cond,offset
if __name__ == '__main__':
    face = FaceDataset(r"/Users/carbenchueng/Desktop/2-Data/Celeba/test_face/48")
    print(face[0])
    # print(face[0][1].shape)
    # print(face[0][2].shape)
