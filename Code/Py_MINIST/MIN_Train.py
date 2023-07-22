import torch
from torchvision import datasets,transforms
from torch.utils.data import DataLoader
from torch.nn.functional import one_hot
from MIN_Net import *
from torch import nn,optim
from torch.utils.tensorboard import SummaryWriter


train_dataset = datasets.MNIST(r"/Users/kabun/Desktop/3-Data",train=True,transform=transforms.ToTensor())
test_dataset = datasets.MNIST(r"/Users/kabun/Desktop/3-Data",train=False,transform=transforms.ToTensor())

train_dataloader = DataLoader(train_dataset,batch_size=512,shuffle=True)
test_dataloader = DataLoader(test_dataset,batch_size=512,shuffle=True)

# print(train_dataset)
if __name__ == '__main__':
    net = Net_v1()
    summerWriter = SummaryWriter("logs")
    # net.load_state_dict(torch.load(""))
    opt = optim.Adam(net.parameters())
    loss_func = nn.MSELoss()
    step = 0
    for epoch in range(1000):
        # acc_sum = 0
        for i,(img,label) in enumerate(train_dataloader):
            img = img.reshape(-1,784)
            label = one_hot(label,10).float()
            # print(type(img))
            # print(type(label))
            out = net(img)

            loss = loss_func(out,label)
            opt.zero_grad()
            loss.backward()
            opt.step()
            layer1_w = net.layre[0].weight
            layer2_w = net.layre[2].weight
            layer3_w = net.layre[4].weight
            layer4_w = net.layre[6].weight
            layer5_w = net.layre[8].weight
            summerWriter.add_histogram("layer1",layer1_w,step)
            summerWriter.add_histogram("layer2",layer2_w,step)
            summerWriter.add_histogram("layer3",layer3_w,step)
            summerWriter.add_histogram("layer4",layer4_w,step)
            summerWriter.add_histogram("layer5",layer5_w,step)
            step+=1

            # out = torch.argmax(out,dim=1)
            # label = torch.argmax(label,dim=1)
            # acc = torch.mean(torch.eq(out,label).float())

            if i%10==0:

                print("train::===>",loss.item())
                # print("acc::===>",acc)
            img = img[:10].reshape(-1,1,28,28)
            summerWriter.add_images("imgs",img,epoch)
            summerWriter.add_scalar("train_loss",loss,epoch)

        for i,(img,label) in enumerate(test_dataloader):
            img = img.reshape(-1,784)
            label = one_hot(label,10).float()
            net.eval()
            out = net(img)
            loss = loss_func(out,label)
            # out = torch.argmax(out,dim=1)
            # label = torch.argmax(label,dim=1)
            # acc = torch.mean(torch.eq(out,label).float())
            # acc_sum+=acc
            if i%100==0:
                print("test::===>",loss.item())
            # print("acc::===>",acc_sum/i)

        # torch.save(net.state_dict(),"epoch.pt")
        #
        torch.save(net.state_dict(),f"./checkpoint/{epoch}.pt")
        print("保存参数成功",epoch)


