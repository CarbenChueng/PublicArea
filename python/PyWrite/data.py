#如何使用pytorch处理自己的数据集
from torch.utils.data import Dataset
import os,cv2,torch
import numpy as np

#创建自己的数据集
class MNISTDataset(Dataset):
    #初始化数据集（将数据集读取进来）
    def __init__(self,root,is_train = True):
        self.dataset = []#记录所有的数据
        sub_dir = "TRAIN" if is_train else "TEST"#根据is_train选择加载的数据集
        for tag in os.listdir(f"{root}/{sub_dir}"):
            img_dir = f"{root}/{sub_dir}/{tag}"
            for img_filename in os.listdir(img_dir):
                img_path = f"{img_dir}/{img_filename}"
                #封装成数据集
                self.dataset.append((img_path,tag))

    #统计数据的个数
    def __len__(self):
        return len(self.dataset)

    #每条数据的处理方式
    def __getitem__(self, index):
        data = self.dataset[index]

        img_data = cv2.imread(data[0],cv2.IMREAD_GRAYSCALE)
        #HWC-->V
        img_data = img_data.reshape(-1)
        #归一化
        img_data = img_data/255

        #one-hot
        tag_one_hot = np.zeros(10)
        tag_one_hot[int(data[1])] = 1

        return torch.tensor(img_data,dtype=torch.float32),torch.tensor(tag_one_hot,dtype=torch.float32)


if __name__ == '__main__':
    dataset = MNISTDataset("data\MNIST_IMG")
    print(dataset[30000][0])