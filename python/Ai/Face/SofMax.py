from torch import nn
from torch.utils import data
from torchvision import transforms
import torch,torchvision,matplotlib.pyplot as plt,os


save_path = "model/net.pth"

class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Sequential(
            nn.Linear(784,512),
            nn.ReLU(),

            nn.Linear(512, 256),
            nn.ReLU(),

            nn.Linear(256, 128),
            nn.ReLU(),

            nn.Linear(128, 2),
            nn.ReLU(),

        )

        self.fc2 = nn.Sequential(adadad
            nn.Linear(2,10)
        )


    def forward(self,x):
        fc1_out = self.fc1(x)
        out = self.fc2(fc1_out)
        return fc1_out,out

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
train_data = torchvision.datasets.MNIST(root="D:\data",download=True,train=True,
                                        transform=transforms.Compose([transforms.ToTensor()]))
train_load = data.DataLoader(dataset=train_data,shuffle=True,batch_size=512)

def vis(feat,labels,epoch):
    plt.ion()
    c = ["#ff0000","#ffff00","#00ff00","#00ffff","#0000ff",
         "#ff00ff","#990000","#999900","#009900","#009999"]
    plt.clf()
    for i in range(10):
        plt.plot(feat[labels==i,0],feat[labels==i,1],".",c=c[i])
    plt.legend(["0","1","2","3","4","5","6","7","8","9"],loc = "upper right")
    # plt.xlim(xmin=-100,xmax = 100)
    # plt.ylim(ymin=-100,ymax = 100)
    plt.title("epoch=%d"%epoch)
    plt.savefig("./images/epoch=%d.jpg"%epoch)
    plt.draw()
    plt.pause(0.001)

if __name__ == '__main__':
    net = Net().to(device)
    if os.path.exists(save_path):
        net = torch.load(save_path)

    loss_func = nn.MSELoss().to(device)
    # opt = torch.optim.Adam(net.parameters())
    opt = torch.optim.SGD(net.parameters(),lr=0.001)

    epoch = 0
    while True:
        feat_loader = []
        laber_loader = []
        for i,(x,y) in enumerate(train_load):
            x = x.view(-1,784).to(device)
            target = torch.zeros(y.size(0),10).scatter_(1,y.view(-1,1),1).to(device)
            # target = y.to(device)
            out_put,feat = net(x)
            loss = loss_func(out_put,target)

            opt.zero_grad()
            loss.backward()
            opt.step()

            feat_loader.append(feat)
            laber_loader.append((y))















