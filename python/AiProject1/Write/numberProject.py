# 如何使用pytorch处理自己的数据
import os, cv2, torch, numpy as np 
from torch.utils.data import Dataset


# 创建自己的数据集
class PictureData(Dataset):
    # 获取数据，初始化数据
    def __init__(self, root, is_train=True):
        self.dataSet = []  # 记录所有数据的路径
        # self.path = root
        # print(self.path)
        subDir = "TRAIN" if is_train else "TEST"
        for tag in os.listdir(f"{root}/{subDir}"):
            imgDir = f"{root}/{subDir}/{tag}"
            # print(imgDir)
            for imgFileName in os.listdir(imgDir):
                imgPath = f"{imgDir}/{imgFileName}"
                # 封装成数据集
                self.dataSet.append((imgPath, tag))
                # print(imgPath)

    # 统计数据的个数
    def __len__(self):

        return len(self.dataSet)

    # 处理数据
    def __getitem__(self, index):

        data = self.dataSet[index]

        imgData = cv2.imread(data[0], cv2.IMREAD_GRAYSCALE)
        # nhwc---->nc
        imgData = (imgData.reshape(-1)) / 255  # 归一化

        # one hot编码
        tagOneHot = np.zeros(10)
        tagOneHot[int(data[1])] = 1

        return torch.tensor(imgData,dtype=torch.float32),torch.tensor(tagOneHot,dtype=torch.float32)


if __name__ == '__main__':
    dataSet = PictureData("/Users/kabun/Desktop/2-python/AiProject1/MNIST_IMG")
    print(dataSet[300][0])
