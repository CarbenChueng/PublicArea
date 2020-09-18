import torch
from torch import nn

class RNN(nn.Module):
    def __init__(self):
        super(RNN, self).__init__()
        self.fc = nn.Sequential(
            nn.Linear(180,128),
            nn.BatchNorm1d(128),
            nn.LeakyReLU()
        )

        self.lstm = nn.LSTM(128,256,2,batch_first=True)
        self.out = nn.Linear(256,10)

    def __forward__(self,x):
        x = x.reshape(-1,180,120).permute(0,2,1)#NCHW--->N,180,120--->N,120,180
        x = x.reshape(-1,180)#N,120,180--->N,180
        fc = self.fc(x)#N,128
        fc = fc.reshape(-1,120,128)#N,128--->N,120,128
        lstm_out,(hn,hc) = self.lstm(fc)#NSV
        out = lstm_out[:,-1,:]#NV

        out = out.reshape(-1,1,246)#NV--->N,1,V
        out = out.expand(-1,4,246)#NV--->N,4,V,expand是广播
        lstm_out,(hn,hc)= self.lstm(out)#N,4,246
        y1 = lstm_out.reshape(-1,246)#N,4,246--->N*4,246
        out = self.out(y1)#N*4,10
        out = out.reshape(-1,4,10)#N*4,10--->N,4,10
        return out














