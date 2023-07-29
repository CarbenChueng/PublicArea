import torch
from torch import nn
import torch.nn.functional as F


class ArcSfotmax(nn.Module):
    def __init__(self,feature,cls_num):
        super(ArcSfotmax, self).__init__()
        self.w = nn.Parameter(torch.randn(feature,cls_num))


    def forward(self,x,s,m):
        x_norm = F.normalize(x,dim=1)
        w_norm = F.normalize(self.w,dim=0)
        cosa = torch.matmul(x_norm*w_norm)/10
        a = torch.arccos(cosa)
        top = torch.exp(s*torch.cos(a+m)*10)
        down = top + torch.sum(torch.exp(s*cosa*10),dim=1,keepdim=True)-torch.exp(s*cosa*10)
        arcsoftmax = top/down
        return arcsoftmax
        # return torch.log(arcsoftmax)