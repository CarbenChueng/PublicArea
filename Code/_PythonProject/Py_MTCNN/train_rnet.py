# 训练R网络

import net
import train

if __name__ == '__main__':
    net = net.RNet()

    trainer = train.Trainer(net, r"./param/rnet.pt", r"/Users/kabun/Desktop/3-Data/Celeba/target/24") # 网络，保存参数，训练数据；创建训练器
    trainer.train()                                                    # 调用训练器中的方法
