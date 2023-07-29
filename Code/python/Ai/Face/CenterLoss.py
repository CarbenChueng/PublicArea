import torch
import torch.nn as nn


class CLoss(nn.Module):
    def __init__(self,cls_num,feat_num):
        super().__init__()

        self.center = nn.Parameter(torch.randn(cls_num,feat_num))

    def forward(self,xs,ys):
        center_exp = self.center.index_select(dim = 0,index=ys.long())
        count = torch.histc(ys)
        return torch.sum(torch.sqrt(torch.sum(torch.pow(2,xs-center_exp),dim=1)))




class test():
    zx = torch.Tensor([[1,1],[2,2],[3,3],[6,6]])
    ys = torch.Tensor([1,2,0,1])
    cente4r = torch.Tensor([[1,2],[2,2],[3,3]])
    cente4r_exp = cente4r.index_select(dim=0,index=ys.long())
    # print(cente4r_exp)
    # print(zx - cente4r_exp)

    # print(zx[ys])
    count = torch.histc(ys.float(),bins=3,min=0,max=2)
    count_exp = count.index_select(dim=0, index=ys.long())
    centet_loss = torch.div(torch.sqrt(torch.sum(torch.pow(2,zx.float()-cente4r_exp.float()),dim=1)),count_exp)
    print(centet_loss)

if __name__ == '__main__':
    tt = test()
    tt
