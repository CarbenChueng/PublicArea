# O网络训练

import net
import train

if __name__ == '__main__':
    net = net.ONet()

    trainer = train.Trainer(net, r"./param/onet.pt", r"/Users/kabun/Desktop/3-Data/Celeba/target/48") # 网络，保存参数，训练数据；创建训器
    trainer.train()                                                     # 调用训练器中的train方法