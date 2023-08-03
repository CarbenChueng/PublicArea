from torch.utils.data import Dataset,DataLoader
from torchvision import transforms
from torch.nn.functional import one_hot
import os,numpy,cv2,torch

class CatDogData(Dataset):

    def __init__(self,root,is_train = True):
        self.data_set = []
        sub_dir = "train" if is_train else "test"
        # print(sub_dir)
        img_dir = f"{root}/{sub_dir}"
        for tag in os.listdir(img_dir):
            img_path = os.path.join(img_dir,tag)
            self.data_set.append((img_path))


    def __len__(self):
        return len(self.data_set)


    def __getitem__(self, item):#默认会多一个批次的纬度
        # pass
        img_path = self.data_set[item]
        img_data = cv2.imread(img_path)
        img_data = transforms.ToTensor()(img_data)
        # img_data = img_data/255
        # print(img_data.shape)
        # img_data = torch.Tensor(img_data).permute(2,0,1)
        # img_data = torch.Tensor(img_data.reshape(100*100*3))
        # print(img_data.shape)

        # print(img_path)
        # print((img_path.split(".")[0][-1]))
        label = int(img_path.split(".")[0][-1])
        label = torch.Tensor([label])
        # print(label)
        # label = torch.squeeze(one_hot(label,2))
        # print(type(img_data),type(label))
        return img_data,label


if __name__ == '__main__':
    cd = CatDogData("/Users/carbenchueng/Desktop/2-Data/Cat_Dog_Img",True)
    print(cd[50])


    # dataload = DataLoader(cd,batch_size=3,shuffle=False)
    # for i,(img,label) in enumerate(dataload):
    #     print(img.shape)
    #     print(label.shape)
    #     exit()
    # ungcode = transforms.ToPILImage
    # img = ungcode(numpy.array(cd[0]))
    # cv2.imshow("asd",cd[0])
    # cv2.waitKey(0)


