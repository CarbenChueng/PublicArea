# 训练P网络

import net
import train

if __name__ == '__main__':
    net = net.PNet()

    trainer = train.Trainer(net, r"./param/pnet.pt", r"/Users/kabun/Desktop/3-Data/Celeba/target/12") # 网络、保存参数、训练数据
    trainer.train()                                                  # 调用训练方法
