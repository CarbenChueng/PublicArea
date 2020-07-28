# 如何使用pytorch处理自己的数据集
from torch.utils.data import Dataset
from PIL import Image
import os, torch, cv2, numpy, matplotlib.pyplot as plt


# 创建自己的数据集
class MNISTDataset(Dataset):
    # 初始化数据，读取数据集
    def __init__(self, root, is_train=True):
        # 记录所有的数据集
        self.CDData = []
        # 选择加载的数据集
        SubDir = "CDTrain" if is_train else "CDTest"
        for tag in os.listdir(f"{root}/{SubDir}"):
            # print(tag)
            ImageDir = f"{root}/{SubDir}/{tag}"
            for ImgFileName in os.listdir(ImageDir):
                ImagePath = f"{ImageDir}/{ImgFileName}"
                #
                #     #展示数据
                # plt.ion()
                # jj = Image.open(ImagePath)
                # plt.imshow(jj)
                # plt.title("Animal")
                # plt.show()
                # plt.pause(1)
                self.CDData.append((ImagePath, ImgFileName[0]))

    # 统计数据的个数
    def __len__(self):

        return len(self.CDData)

    # 每一条数据的处理方式

    def __getitem__(self, item):
        data = self.CDData[item]
        # print(data)
        ImaData = cv2.imread(data[0], cv2.IMREAD_GRAYSCALE)
        # print(ImaData)
        # NHWC
        ImaData = ImaData.reshape(-1) / 255.
        # onehot
        TagOneHot = numpy.zeros(2)
        # print(TagOneHot)
        TagOneHot[int(data[1])] = 1
        # TagOneHot=int(data[1])
        return torch.tensor(ImaData,dtype=torch.float32),\
               torch.tensor(TagOneHot,dtype=torch.float32)


if __name__ == '__main__':
    dada = MNISTDataset("D:\PyCharmProject\HomeWork\CatDog\CDData")

    print(dada[2000][0])
