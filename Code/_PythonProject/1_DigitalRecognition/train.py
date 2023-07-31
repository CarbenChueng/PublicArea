from torch.utils.data import DataLoader
from torch import optim
from data import *
from net import *
import torch
# from torch.utils.tensorboard import SummaryWriter


DEVIDE = "cuda:0"#显卡序列号


class Train(object):

    def __init__(self,root):
        self.train_data_set = MinistData(root,True)
        self.train_data_loader = DataLoader(self.train_data_set,batch_size=2,shuffle=True)

        self.test_data_set = MinistData(root,False)
        self.test_data_loader = DataLoader(self.test_data_set,batch_size=2,shuffle=True)

        self.net = Net()
        self.opt = optim.Adam(self.net.parameters())
        self.loss_func = MSELoss()

    def __call__(self, *args, **kwargs):
        for epoch in range(10000):
            for i,(img,tag) in enumerate(self.train_data_loader):
                #开启训练模式（默认会调用）
                self.net.train()
                y = self.net.forward(img)
                # print(y)
                # print(tag)
            #     print("="*20+">>out",torch.argmax(y,dim=1))
            #     print("="*20+">>tag",torch.argmax(tag,dim=1))
                loss = self.loss_func(y,tag)

                self.opt.zero_grad()
                loss.backward()
                self.opt.step()
                if i %250 == 0:
                    print("="*10+">>train_loss:  ",loss.item())

            #
            for i,(img,tag) in enumerate(self.test_data_loader):
                #开启测试模式（必须手动调用）
                self.net.eval()
                test_y = self.net.forward(img)
                loss = torch.mean((tag-test_y)**2)

                predick_tag = torch.argmax(test_y,dim=1)
                label_tag = torch.argmax(tag,dim=1)
                acc = torch.mean(torch.eq(predick_tag,label_tag).float())
                if i %100 == 0:
                    print("="*10+">>test_loss:  ",loss.item())
                    print("="*10+">>acc:  ",acc.item())



if __name__ == '__main__':
    train = Train("/Users/carbenchueng/Desktop/2-Data/MNIST_IMG")
    train()


