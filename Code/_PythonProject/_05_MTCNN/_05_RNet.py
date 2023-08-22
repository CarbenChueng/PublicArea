from _05_Net import RNet
from _05_Train import Trainer


if __name__ == '__main__':
    r_net = RNet()
    trainer = Trainer(r_net, "parameter/rnet.pt", "/Users/carbenchueng/Desktop/2-Data/Celeba/target/24")
    trainer.train()