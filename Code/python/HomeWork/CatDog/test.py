from torch import jit
from CDNet import Netv3
import torch


if __name__ == '__main__':
    model = Netv3()
    model.load_state_dict(torch.load("checkPoint0.t"))
    # out = model(x)

    # 虚拟一个输入
    CDinput = torch.randn(1,10000)
    torchModel = jit.trace(model,CDinput)
    torchModel.save("sjsj.pt")


# a = [1,2,3,4,6,7,78]
# for x in enumerate(a):
#     print(x)
