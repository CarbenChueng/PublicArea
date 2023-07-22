from MIN_Net import Net_v1
from torch.utils.tensorboard import SummaryWriter
import torch,time

if __name__ == '__main__':
    net = Net_v1()
    net.load_state_dict(torch.load("./checkpoint/1.pt"))
    # print(net)
    summerWriter = SummaryWriter("logs")
    # print(net.layre[0].weight)
    # print(net.layre[0].bias)
    layer1_w = net.layre[0].weight
    layer2_w = net.layre[2].weight
    layer3_w = net.layre[4].weight
    layer4_w = net.layre[6].weight
    layer5_w = net.layre[8].weight

    summerWriter.add_histogram("layer1",layer1_w)
    summerWriter.add_histogram("layer1",layer2_w)
    summerWriter.add_histogram("layer1",layer3_w)
    summerWriter.add_histogram("layer1",layer4_w)
    summerWriter.add_histogram("layer1",layer5_w)
    # print("写入完成！！！")
    time.sleep(2)

    #权重初始化
    # conv = torch.nn.Conv2d(3,16,3,1,0)
    # print(conv.weight.shape)

    # torch.nn.init.kaiming_normal_(conv.weight)
    # torch.nn.init.normal_(conv.weight,0,0.1)
    # torch.nn.init.zeros_(conv.weight)
    # print(conv.weight)

    #对整一层权重初始化
    # def weight_init(m):
    #     if(isinstance(m,torch.nn.Conv2d)):
    #         torch.nn.init.kaiming_normal_(m.weight)
    #         if m.bias is not None:
    #             torch.nn.init.zeros_(m.bias)
    #     elif(isinstance(m,torch.nn.Linear)):
    #         torch.nn.init.normal_(m.weight0,0,0.5)
    #         if m.bias is not None:
    #             torch.nn.init.zeros_(m.bias)