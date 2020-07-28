from AiProject1.Write.net import NetV1
from torch import jit
import torch

if __name__ == '__main__':
    model = NetV1()
    model.load_state_dict(torch.load("checkPoint/3.pkl"))
    
    
    #虚拟一个输入，做占位
    inputt = torch.randn(1,784)
    torchModel = jit.trace(model,inputt)
    torchModel.save("mnistNet.pt")