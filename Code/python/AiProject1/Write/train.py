from AiProject1.Write.numberProject import PictureData
from AiProject1.Write.net import *
from torch.utils.data import DataLoader
from torch import optim
import torch
# from torch.utils.tensorboard import SummaryWriter


DEVIDE = "cuda:0"#显卡序列号

class Train():
    # 训练准备（获取数据）
    def __init__(self, root):
        # self.summaryWriter = SummaryWriter("./logs")


        # 训练集
        self.trainDataSet = PictureData(root)
        self.trainDataLoad = DataLoader(self.trainDataSet, batch_size=100, shuffle=True, num_workers=8)  # shuffle是不放回抽样

        # 验证集
        self.testDataSet = PictureData(root, is_train=False)
        self.testDataLoad = DataLoader(self.testDataSet, batch_size=100, shuffle=True, num_workers=8)  # shuffle是不放回抽样

        # 创建模型
        self.net = Netv6()

        #加载训练参数
        # self.net.load_state_dict(torch.load("checkPoint/3.pkl"))
        self.opt = optim.Adam(self.net.parameters())  # 根据学习情况自动调整

    # 训练代码
    def __call__(self, *args, **kwargs):
        for epoch in range(1000000):
            loss_sum = 0.
            for i, (img, tage) in enumerate(self.trainDataLoad):
                trainY = self.net(img)
                loss = torch.mean((tage - trainY) ** 2)

                # 训练三件套
                self.opt.zero_grad()
                loss.backward()
                self.opt.step()
                # print(loss)
                loss_sum += loss.detach().item()
            trainAvgLoss = loss_sum / len(self.trainDataLoad)

            # 验证
            sumScore = 0.
            testLossSum = 0.
            for i, (img, tage) in enumerate(self.testDataLoad):
                testY = self.net(img)
                loss = torch.mean((tage - testY) ** 2)

                testLossSum += loss.item()

                preTage = torch.argmax(testY,dim=1)#将onehot转为标签值
                labelTage=  torch.argmax(tage,dim=1)
                sumScore += torch.sum(torch.eq(preTage, labelTage).float())
            score = sumScore/len(self.testDataSet)
            testAvgLoss = testLossSum / len(self.testDataLoad)

            # self.summaryWriter.add_scalars("loss",{"trainAvgLoss:":trainAvgLoss,"testAvgLoss:":testAvgLoss},epoch)
            # self.summaryWriter.add_scalar("score",score,epoch)

            print("epoch:",epoch,"trainAvgLoss:",trainAvgLoss,"testAvgLoss:",testAvgLoss,"score:",score)
            #保存参数
            # torch.save(self.net.state_dict(),f"./checkPoint/{epoch}.pkl")


if __name__ == '__main__':
    train = Train("/Users/kabun/Desktop/2-python/AiProject1/MNIST_IMG")
    train()
