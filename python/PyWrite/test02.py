from torch import jit
from net import Netv1
import torch

if __name__ == '__main__':
    model = Netv1()
    model.load_state_dict(torch.load("checkpoint/3.t"))

    #虚拟一个输入（占位）
    input = torch.randn(1,784)

    torch_model = jit.trace(model,input)
    torch_model.save("mnist_net.pt")