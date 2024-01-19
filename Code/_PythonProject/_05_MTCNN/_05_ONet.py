from _05_Net import ONet
from _05_Train import Trainer


if __name__ == '__main__':
    o_net = ONet()
    trainer = Trainer(o_net, "parameter/onet.pt", "/Users/carbenchueng/Desktop/2-Data/Celeba/target/48")
    trainer.train()
