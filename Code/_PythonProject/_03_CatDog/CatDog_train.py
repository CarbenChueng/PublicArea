from torchvision import datasets,transforms
from CatDog_data import *
from torch.backends import mps
from tqdm import tqdm
from torch.utils.tensorboard import SummaryWriter
from torch.utils.data import Dataset,DataLoader
from torchvision import datasets,transforms
from torch.nn.functional import one_hot
from CAtDog_net import *

DEVICE = "mps"

train_data_set = CatDogData("/Users/carbenchueng/Desktop/2-Data/Cat_Dog_Img")
# test_data_set =
train_data_loader = DataLoader(train_data_set,batch_size=1000,shuffle=True)
# test_data_loader = DataLoader(test_data_set,batch_size=1000,shuffle=True)

if __name__ == '__main__':
    sum_write = SummaryWriter("logs")
    net = Net().to(DEVICE)
    # net.load_state_dict(torch.load("./prarm/39.pt"))
    opt = torch.optim.Adam(net.parameters())
    loss_func = MSELoss()
    for epoch in tqdm(range(10000)):
        acc_sum = 0
        for i,(img,label) in enumerate(train_data_loader):
            label = label.float()
            img,label = img.to(DEVICE),label.to(DEVICE)
            # print(img.shape,label,sep="\n")

            out = net(img)
            train_loss = loss_func(out,label)
            opt.zero_grad()
            train_loss.backward()
            opt.step()

            if i%100 == 0:
                print("==========>train_loss",train_loss.item())
            sum_write.add_scalar("train_loss",train_loss.item(),epoch)

        # for i,(img,tag) in enumerate(test_data_loader):
        #     net.eval()
        #     #img(n,1,32,32)=====>(n,32*32*3)
        #     img = img.reshape(-1,32*32*3)
        #     label = one_hot(tag,10).float()
        #     # img,label = img.to(DEVICE),label.to(DEVICE)
        #     # print(img.shape,label.shape,sep="\n")
        #
        #     out = net(img)
        #     test_loss = loss_func(out,label)
        #     out = torch.argmax(out,dim=1)
        #     label = torch.argmax(label,dim=1)
        #     acc = torch.mean(torch.eq(out,label).float())
        #     acc_sum+=acc
        #
        #     if i%100 == 0:
        #         print("==========>test_loss",test_loss.item())
        #     sum_write.add_scalar("test_loss",test_loss.item(),epoch)
        # print("==========>acc",acc_sum/i)
        # sum_write.add_scalars("loss",{"train_loss":train_loss,"test_loss":test_loss},epoch)
        # torch.save(net.state_dict(),f"./prarm/{epoch}.pt")