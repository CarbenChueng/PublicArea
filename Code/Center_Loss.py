import torch,torchvision
from torch import nn
from torchvision import transforms
from matplotlib import pyplot as plt
from torch.utils import data

class CenterLoss(nn.Module):
    def __init__(self,cls_num,feature_num):
        super(CenterLoss, self).__init__()

        self.cls_num = cls_num
        self.center = nn.Parameter(torch.randn(cls_num,feature_num))

    def forward(self,xs,ys):
        center_exp = self.center.index_select(dim=0,index = ys.long())
        count = torch.histc(ys,bins=self.cls_num,min=0,max=self.cls_num-1)
        count_exp = count.index_select(dim=0,index = ys.long())
        center_loss = torch.sqrt(torch.sum(torch.pow(xs-center_exp,2),dim=1))
        center_loss = torch.sum(torch.div(center_loss,count_exp))
        return center_loss

class MainNet(nn.Module):
    def __init__(self,):
        super(MainNet, self).__init__()
        self.Hid_layer = nn.Sequential(
            nn.Linear(784,120),
            nn.LeakyReLU(),

            nn.Linear(120,2),
        )
        self.Output_layer = nn.Sequential(
            nn.Linear(2,10)
        )
        self.center_loss_layer = CenterLoss(10,2)
        self.crossentr = nn.CrossEntropyLoss()

    def forward(self,xs):
        features = self.Hid_layer(xs)
        outputs = self.Output_layer(features)
        return features,outputs

    def getloss(self,outputs,features,labels):
        loss_cls = self.crossentr(outputs,labels)
        loss_center = self.center_loss_layer(features,labels)
        loss = loss_cls+loss_center
        return loss

train_data = torchvision.datasets.MNIST(r"/Users/kabun/Desktop/3-Data",train=True,transform=transforms.ToTensor())
# train_data = torchvision.datasets.CIFAR10(r"/Users/kabun/Desktop/3-Data/CIFA10",train=True,transform=transforms.ToTensor(),download=False)
train_loader = data.DataLoader(dataset=train_data,shuffle=True,batch_size=512)
if __name__ == '__main__':
    net = MainNet()
    opt = torch.optim.Adam(net.parameters())
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    for i ,(x,y) in enumerate(train_loader):
        x = x.reshape(-1,784).to(device)
    # target = one_hot(y,10).to(device).float()
        target = y.to(device)

        feat,out_put = net(x)
        loss = net.getloss(out_put,feat,target)
        opt.zero_grad()
        loss.backward()
        opt.step()
        if i%100==0:
            print(loss.item())
