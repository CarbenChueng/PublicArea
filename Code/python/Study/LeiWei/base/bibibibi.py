import torch,os,torchvision
from torch import nn
from torchvision import transforms
from matplotlib import pyplot as plt
from torch.utils import data
from torch.nn.functional import one_hot

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        # self.fc1 = nn.Sequential(
        #     nn.Conv2d(1,16,3),
        #     nn.LeakyReLU(),
        #
        #     nn.Conv2d(16,32,3),
        #     nn.LeakyReLU(),
        #
        #     nn.Conv2d(32,64,3),
        #     nn.LeakyReLU(),
        #
        # )
        #
        # self.fc2 = nn.Sequential(
        #     nn.Linear(64*22*22,10),
        # )

        self.fc1 = nn.Sequential(
            nn.Linear(784,512,bias=False),
            nn.BatchNorm1d(512),
            nn.LeakyReLU(),

            nn.Linear(512,256,bias=False),
            nn.BatchNorm1d(256),
            nn.LeakyReLU(),

            nn.Linear(256,128,bias=False),
            nn.BatchNorm1d(128),
            nn.LeakyReLU(),
            nn.Linear(128,2),
        )
        self.fc2 = nn.Sequential(
            nn.Linear(2,10),
        )

    def forward(self,x):
        out1 = self.fc1(x)
        # out = out1.reshape(-1,64*22*22)
        out = self.fc2(out1)
        return out1,out

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(device)

train_data = torchvision.datasets.MNIST(r"/Users/kabunchueng/Desktop/3-Data",train=True,transform=transforms.ToTensor())
# train_data = torchvision.datasets.CIFAR10(r"/Users/kabun/Desktop/3-Data/CIFA10",train=True,transform=transforms.ToTensor(),download=False)
train_loader = data.DataLoader(dataset=train_data,shuffle=True,batch_size=512)
# test_data = torchvision.datasets.MNIST(r"/Users/kabun/Desktop/3-Data",train=False,transform=transforms.ToTensor())
# test_data = torchvision.datasets.MNIST(r"/Users/kabun/Desktop/3-Data",train=False,transform=transforms.ToTensor())

#特征可视化
def visualize(feat,labels,epoch):
    plt.ion()
    c = ["#ff0000","#ffff00","#00ffff","#0000ff","#ff00ff",
         "#990000","#009900","#999900","#009999","#00ff00",]
    plt.clf()
    for i in range(10):
        plt.plot(feat[labels==i,0],feat[labels==i,1],".",c=c[i])
    plt.legend(["0","1","2","3","4","5","6","7","8","9"],loc = "upper right")
    plt.title("epoch = %d"%epoch)
    plt.savefig("images/epoch_bn=%d.jpg"%epoch)
    plt.draw()
    plt.pause(0.001)

if __name__ == '__main__':
    net = Net().to(device)
    # x = torch.randn(1,1,28,28)
    # y = net(x)
    # print(y.shape)
    # loss_func = nn.MSELoss()
    loss_func = nn.CrossEntropyLoss()
    opt = torch.optim.Adam(net.parameters())
    # opt = torch.optim.SGD(net.parameters(),lr=0.01,momentum=0.5)

    epoch = 0
    while True:
        feat_loader = []
        label_loader = []
        for i ,(x,y) in enumerate(train_loader):
            x = x.reshape(-1,784).to(device)
            # target = one_hot(y,10).to(device).float()
            target = y.to(device)

            feat,out_put = net(x)
            loss = loss_func(out_put,target)
            opt.zero_grad()
            loss.backward()
            opt.step()

            feat_loader.append(feat)
            label_loader.append(y)

            if i % 10 ==0:
                print(loss.item())

        feat = torch.cat(feat_loader,0)
        labels = torch.cat(label_loader,0)
        visualize(feat.detach().cpu().numpy(),labels.detach().cpu().numpy(),epoch)
        epoch+=1


