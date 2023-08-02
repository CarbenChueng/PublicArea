from torch.nn import *
from torch.backends import mps
from tqdm import tqdm
from torch.utils.tensorboard import SummaryWriter
from torch.utils.data import Dataset,DataLoader
from torchvision import datasets,transforms
from torch.nn.functional import one_hot
from write_net import *

DEVICE = "mps"

train_data_sat = datasets.MNIST(root="/Users/carbenchueng/Desktop/2-Data",
                                train=True,download=False,
                                transform=transforms.ToTensor())
test_data_sat = datasets.MNIST(root="/Users/carbenchueng/Desktop/2-Data",
                                train=False,download=False,
                                transform=transforms.ToTensor())
train_loader = DataLoader(train_data_sat,batch_size=1000,shuffle=True)
test_loader = DataLoader(test_data_sat,batch_size=100,shuffle=True)
#显示数据集类别  classes
# print(train_data_sat.classes)
# img_data = train_data_sat.data[0]
# uncode = transforms.ToPILImage()
# img = uncode(img_data)
# img.show()
# print(train_data_sat.targets[0])

if __name__ == '__main__':
    sum_write = SummaryWriter("logs")
    net = Net()
    net.load_state_dict(torch.load("./prarm/2.t"))
    opt = torch.optim.Adam(net.parameters())
    loss_func = MSELoss()
    for epoch in tqdm(range(10000)):
        acc_sum = 0
        for i,(img,label) in enumerate(train_loader):
            #img(n,1,28,28)=====>(n,784)
            # img = img.reshape(-1,784)
            label = one_hot(label,10).float()
            # print(img.shape,label,sep="\n")

            out = net(img)
            train_loss = loss_func(out,label)
            opt.zero_grad()
            train_loss.backward()
            opt.step()

            if i%100 == 0:
                print("==========>train_loss",train_loss.item())
            # sum_write.add_scalar("train_loss",train_loss.item(),epoch)

        for i,(img,label) in enumerate(test_loader):
            net.eval()
            #img(n,1,28,28)=====>(n,784)
            # img = img.reshape(-1,784)
            label = one_hot(label,10).float()
            # print(img.shape,label.shape,sep="\n")

            out = net(img)
            test_loss = loss_func(out,label)
            out = torch.argmax(out,dim=1)
            label = torch.argmax(label,dim=1)
            acc = torch.mean(torch.eq(out,label).float())
            # acc_sum+=acc

            if i%100 == 0:
                # print("==========>test_loss",test_loss.item())
                print("==========>acc       ",acc)
            # sum_write.add_scalar("test_loss",test_loss.item(),epoch)
        # print("==========>acc",acc_sum/i)
        # sum_write.add_scalars("loss",{"train_loss":train_loss,"test_loss":test_loss},epoch)
        # torch.save(net.state_dict(),f"./prarm/{epoch}.t")