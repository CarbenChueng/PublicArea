import torch,numpy,os,cv2
from torch.utils.data import Dataset,DataLoader


class MinistData(Dataset):

    def __init__(self,root,is_train=True):
        self.data_set = []
        sub_dir = "TRAIN" if is_train else "TEST"
        for tag in os.listdir(f"{root}/{sub_dir}"):
            img_dir = f"{root}/{sub_dir}/{tag}"
            # print(img_dir)
            for img_name in os.listdir(img_dir):
                # print(img_name)
                img_path = f"{root}/{sub_dir}/{tag}/{img_name}"
                # print(img_path)
                self.data_set.append((img_path,tag))
                # return img_path,tag


    def __len__(self):
        return len(self.data_set)

    def __getitem__(self, item):
        #每条数据的处理方式
        data = self.data_set[item]
        img_data = cv2.imread(data[0],0)
        img_data = img_data.reshape(-1)
        img_data = img_data/255

        #one_hot
        tag_one_hot = numpy.zeros(10)
        tag_one_hot[int(data[1])] = 1
        return torch.tensor(img_data,dtype=torch.float32),torch.tensor(tag_one_hot,dtype=torch.float32)
        # return numpy.float32(img_data),numpy.float32(tag_one_hot)

if __name__ == '__main__':
    data = MinistData("/Users/carbenchueng/Desktop/2-Data/MNIST_IMG")
    # print(data[3333])
    # print(data[3333])
    data_loader = DataLoader(dataset=data,batch_size=5,shuffle=True)
    for i,(x,y) in enumerate(data_loader):
        print(f"===>{i}" ,x.shape ,y.shape)
