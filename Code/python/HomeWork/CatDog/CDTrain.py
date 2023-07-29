from CDData import *
from CDNet import *
from torch.utils.data import DataLoader
from torch import optim
from torch.utils.tensorboard import SummaryWriter
from tqdm import tqdm

DEVICE = "cuda:0"

class Train():

    # 获取训练集
    def __init__(self, path):

        self.sumwr = SummaryWriter("./logs")

        self.trianDataSet = MNISTDataset(path)
        self.trianDataLoad = DataLoader(self.trianDataSet, batch_size=100, shuffle=True)

    # 获取测试集

        self.testDataSet = MNISTDataset(path,is_train=False)
        self.testDataLoad = DataLoader(self.testDataSet, batch_size=100, shuffle=False)

        # 创建模型
        self.net = Netv3()
        #加载训练参数
        # self.net.load_state_dict(torch.load(f"./checkPoint0.t"))
        self.net.to(DEVICE)
        self.opt = optim.Adam(self.net.parameters())

    # 训练
    def __call__(self, *args, **kwargs):
        for epoch in range(1000000):
            # 训练
            trainLossSum = 0
            for x,(img,tage) in enumerate(tqdm(self.trianDataLoad)):
                img = img.to(DEVICE)
                tage = tage.to(DEVICE)

                trainY = self.net(img)

                loss = torch.mean((tage-trainY)**2)

                loss.backward()
                self.opt.step()
                trainLossSum+=loss.cpu().detach().item()
            trainAvgLoss = trainLossSum/len(self.trianDataLoad)


            #验证
            sumScore = 0
            testLossSum = 0
            for x,(img,tage) in enumerate(tqdm(self.testDataLoad)):
                img = img.to(DEVICE)
                tage = tage.to(DEVICE)

                testY = self.net(img)

                loss = torch.mean((tage-testY)**2)
                testLossSum+=loss.item()
                # 将onehot转为标签值
                preTage = torch.argmax(testY,dim=1)
                lableTage = torch.argmax(tage,dim=1)

                sumScore+=torch.sum(torch.eq(preTage,lableTage).float())
            score = sumScore/len(self.testDataSet)
            testAvgLoss = testLossSum/len(self.testDataLoad)

            self.sumwr.add_scalars("loss",
                                   {"trainLoss":trainAvgLoss,"testLoss":testAvgLoss},
                                   epoch)

            self.sumwr.add_scalar("score",score,epoch)


            print(epoch,trainAvgLoss,testAvgLoss,score.item())

            #保存参数
            # torch.save(self.net.state_dict(),f"./checkPoint{epoch}.t")



if __name__ == '__main__':
    train = Train("D:\PyCharmProject\HomeWork\CatDog\CDData")
    train()
