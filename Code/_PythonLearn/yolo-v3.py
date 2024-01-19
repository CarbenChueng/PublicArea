from torch.nn import *
import torch

class UpSamplePlayer(Module):

    def forward(self,x):
        return functional.interpolate(x,scale_factor=2,mode="nearrest")

class DownSamplePlayer(Module):

    def __init__(self,in_chancel,out_chancel,):
        super(DownSamplePlayer, self).__init__()
        self.down_layer = Sequential(
            ConvolutionLayer(in_chancel,out_chancel,3,2,1)
        )

    def forward(self,x):
        return self.down_layer(x)

class ConvolutionLayer(Module):

    def __init__(self,in_chancel,out_chancel,ker,stride,padding,bias=False):
        super(ConvolutionLayer, self).__init__()
        self.down_layer = Sequential(
            Conv2d(in_chancel,out_chancel,ker,stride,padding,bias),
            BatchNorm2d(out_chancel),
            LeakyReLU()
        )

    def forward(self,x):
        return self.down_layer(x)

class ResLayer(Module):

    def __init__(self,in_chancel)->None:
        super(ResLayer, self).__init__()
        self.res_layer = Sequential(
            ConvolutionLayer(in_chancel,in_chancel//2,1,1,0),
            ConvolutionLayer(in_chancel//2,in_chancel,3,1,1)
        )

    def forward(self,x):
        return self.res_layer(x)


class ConvolutionSet(Module):

    def __init__(self,in_chancel,out_chancel):
        super(ConvolutionSet, self).__init__()
        self.conv_set_layer = Sequential(
            ConvolutionLayer(in_chancel,out_chancel,1,1,0),
            ConvolutionLayer(out_chancel,in_chancel,3,1,0),
            ConvolutionLayer(in_chancel,out_chancel,1,1,0),
            ConvolutionLayer(out_chancel,in_chancel,3,1,0),
            ConvolutionLayer(in_chancel,out_chancel,1,1,0),
        )

    def forward(self,x):

        return self.conv_set_layer(x)


class DarkNet53(Module):

    def __init__(self):
        super(DarkNet53, self).__init__()
        self.truk_52 = Sequential(
            ConvolutionLayer(3,32,3,1,1),
            ConvolutionLayer(32,64,3,2,1),
            ResLayer(64),
            DownSamplePlayer(64,128),
            ResLayer(128),
            ResLayer(128),
            DownSamplePlayer(128,256),
            ResLayer(256),
            ResLayer(256),
            ResLayer(256),
            ResLayer(256),
            ResLayer(256),
            ResLayer(256),
            ResLayer(256),
            ResLayer(256),

        )

        self.truk_26 = Sequential(
            DownSamplePlayer(256,512),
            ResLayer(512),
            ResLayer(512),
            ResLayer(512),
            ResLayer(512),
            ResLayer(512),
            ResLayer(512),
            ResLayer(512),
            ResLayer(512),
        )

        self.truk_13 = Sequential(
            DownSamplePlayer(512,1024),
            ResLayer(1024),
            ResLayer(1024),
            ResLayer(1024),
            ResLayer(1024),
        )

        self.conv_13 = Sequential(
            ConvolutionSet(1024,512),
        )

        self.detetion_13 = Sequential(
            ConvolutionLayer(512,1024,3,1,1),
            Conv2d(1024,45,1,1,0)
        )

        self.up_26 = Sequential(
            ConvolutionLayer(512,256,3,1,1),
            UpSamplePlayer()
        )

        self.conv_26 = Sequential(
            ConvolutionSet(768,256),
        )

        self.detetion_26 = Sequential(
            ConvolutionLayer(256,512,3,1,1),
            Conv2d(512,45,1,1,0)
        )

        self.up_52 = Sequential(
            ConvolutionLayer(256,128,3,1,1),
            UpSamplePlayer()
        )

        self.conv_52 = Sequential(
            ConvolutionSet(384,128),
        )

        self.detetion_52 = Sequential(
            ConvolutionLayer(128,256,3,1,1),
            Conv2d(256,45,1,1,0)
        )

    def forward(self,x):
        h_52 = self.truk_52(x)
        h_26 = self.truk_26(x)
        h_13 = self.truk_13(x)

        conv_set_13 = self.conv_13(h_13)
        detetion_13 =  self.detetion_13(conv_set_13)

        up_out_26 = self.up_26(conv_set_13)
        route_out_26 = torch.cat((up_out_26,h_26),dim=1)

        conv_set_26 = self.conv_26(route_out_26)
        detetion_26 =  self.detetion_26(conv_set_26)

        up_out_52 = self.up_52(conv_set_26)
        route_out_52 = torch.cat((up_out_52,h_52),dim=1)

        conv_set_52 = self.conv_52(route_out_52)
        detetion_52 =  self.detetion_52(conv_set_52)

        return detetion_13,detetion_26,detetion_52


if __name__ == '__main__':
    yolo3 = DarkNet53()
    x = torch.randn(6,3,416,416)
    y = yolo3(x)

    print(y[0].shape)
    print(y[1].shape)
    print(y[2].shape)