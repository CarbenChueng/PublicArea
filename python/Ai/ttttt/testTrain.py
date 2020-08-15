from Ai.ttttt.testNet import *
from torch.utils.data import DataLoader
from torch import optim
import torch
from Ai.ttttt.testData import MyDataSet

DEVICE = "cuda:0"#显卡序列号

class Train():
    # 训练准备（获取数据）
    def __init__(self):
        # self.summaryWriter = SummaryWriter("./logs")


        # 训练集
        self.trainDataSet = MyDataSet("D:\data\CDData\CDTrain\Cat")
        self.trainDataLoad = DataLoader(self.trainDataSet, batch_size=100, shuffle=True, num_workers=8)  # shuffle是不放回抽样

        # 验证集
        self.testDataSet = MyDataSet("D:\data\CDData\CDTest\Cat")
        self.testDataLoad = DataLoader(self.testDataSet, batch_size=100, shuffle=False, num_workers=8)  # shuffle是不放回抽样

        # 创建模型
        self.net = Netv6()
        self.net = self.net.to(DEVICE)

        #加载训练参数
        # self.net.load_state_dict(torch.load("checkPoint/3.pkl"))
        # self.opt = optim.Adam(self.net.parameters())  # 根据学习情况自动调整
        self.opt = optim.SGD(self.net.parameters(),lr=0.001)  # 根据学习情况自动调整
        self.loss_func = nn.MSELoss()


    # 训练代码
    def __call__(self, *args, **kwargs):
        for epoch in range(100000):
            loss_sum = 0.
            for i, (img, tage) in enumerate(self.trainDataLoad):
                img,tage = img.to(DEVICE),tage.to(DEVICE)
                # print(type(img))
                # print(img.shape)
                out = self.net(img)

                tage = nn.functional.one_hot(tage.long(),2)
                tage = torch.squeeze(tage)
                loss = self.loss_func(out,tage.float())
                # print(loss)

                # 训练三件套
                self.opt.zero_grad()
                loss.backward()
                self.opt.step()
                # print(loss)
                loss_sum += loss.detach().item()
                if i%20 == 0:
                    print(loss.item())
            trainAvgLoss = loss_sum / len(self.trainDataLoad)
            print(trainAvgLoss)


            # 验证
            # sumScore = 0.
            # testLossSum = 0.
            # for i, (img, tage) in enumerate(self.testDataLoad):
            #     img,tage = img.to(DEVIDE),tage.to(DEVIDE)
            #     testY = self.net(img)
            #     tage = nn.functional.one_hot(tage.long(), 2)
            #     loss = self.loss_func(tage,testY)
            #
            #     testLossSum += loss.cpu().item()
            #
            #     preTage = torch.argmax(testY,dim=1)#将onehot转为标签值
            #     labelTage=  torch.argmax(tage,dim=1)
            #     sumScore += torch.sum(torch.eq(preTage, labelTage).float())
            #     if i%100==0:
            #         print(loss.item(),torch.mean(torch.eq(preTage, labelTage).float()).item())
            # score = sumScore/len(self.testDataSet)
            # testAvgLoss = testLossSum / len(self.testDataLoad)

            # self.summaryWriter.add_scalars("loss",{"trainAvgLoss:":trainAvgLoss,"testAvgLoss:":testAvgLoss},epoch)
            # self.summaryWriter.add_scalar("score",score,epoch)

            # print("epoch:",epoch,"trainAvgLoss:",trainAvgLoss,"testAvgLoss:",testAvgLoss,"score:",score)
            #保存参数
            # torch.save(self.net.state_dict(),f"./checkPoint/{epoch}.pkl")


if __name__ == '__main__':
    train = Train()
    train()
