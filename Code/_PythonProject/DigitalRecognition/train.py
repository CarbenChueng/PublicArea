from torch.utils.data import DataLoader
from torch.backends import mps
from torch import optim
from tqdm import tqdm
from data import *
from net import *
import torch,os
from torch.utils.tensorboard import SummaryWriter


DEVIDE = "mps"


class Train:

    # def __init__(self,root,save_path):
    def __init__(self,root):
        self.test_loss = 0
        self.train_loss = 0
        self.summar_writer = SummaryWriter("logs")

        self.train_data_set = MinistData(root,True)
        self.train_data_loader = DataLoader(self.train_data_set,batch_size=2,shuffle=True)

        self.test_data_set = MinistData(root,False)
        self.test_data_loader = DataLoader(self.test_data_set,batch_size=2,shuffle=True)

        self.net = Net_v1().to(DEVIDE)
        # if os.path.exists(save_path):
        #加载预训练权重
            # self.net.load_state_dict(torch.load(save_path))
        self.opt = optim.Adam(self.net.parameters())
        self.loss_func = MSELoss()
        self.train = True

    def __call__(self, *args, **kwargs):
        index = 0
        index1 = 0
        for epoch in range(100):
            # if self.train:
            for i,(img,tag) in enumerate(self.train_data_loader):
                #开启训练模式（默认会调用）
                img,tag = img.to(DEVIDE),tag.to(DEVIDE)
                self.net.train()
                y = self.net.forward(img)
                # print(y)
                # print(tag)
            #     print("="*20+">>out",torch.argmax(y,dim=1))
            #     print("="*20+">>tag",torch.argmax(tag,dim=1))
                train_loss = self.loss_func(y,tag)

                self.opt.zero_grad()
                train_loss.backward()
                self.opt.step()

                if i %500 == 0:
                    print("="*10+">>train_loss:  ",train_loss.item())
                #收集损失
                self.summar_writer.add_scalar("train_loss",train_loss,index)
                index += 1


        # else:
            #验证
            # for i,(img,tag) in enumerate(self.test_data_loader):
            #     #开启测试模式（必须手动调用）
            #     img,tag = img.to(DEVIDE),tag.to(DEVIDE)
            #     self.net.eval()
            #     test_y = self.net.forward(img)
            #     test_loss = torch.mean((tag-test_y)**2)
            #
            #     predick_tag = torch.argmax(test_y,dim=1)
            #     label_tag = torch.argmax(tag,dim=1)
            #     acc = torch.mean(torch.eq(predick_tag,label_tag).float())
            #     if i %500 == 0:
            #         print("="*10+">>test_loss:  ",test_loss.item())
            #         print("="*10+">>acc:        ",acc.item())
            #     self.summar_writer.add_scalar("test_loss",test_loss,index1)
            #     index1+=1
            # self.summar_writer.add_scalars("loss", {"train_loss":train_loss,"test_loss":test_loss},epoch)
        #保存参数
        # torch.save(self.net.state_dict(),f"prarm/{epoch}.pt")

if __name__ == '__main__':
    # train = Train("/Users/carbenchueng/Desktop/2-Data/MNIST_IMG",save_path="prarm/0.pt")
    train = Train("/Users/carbenchueng/Desktop/2-Data/MNIST_IMG")
    train()


