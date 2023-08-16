from torch.nn import *

class PNet(Module):
    def __init__(self):
        super(PNet, self).__init__()
        self.layers = Sequential(
            Conv2d(3,10,3),
            PReLU(),
            MaxPool2d(3),
            Conv2d(10,16,3),
            PReLU(),
            Conv2d(16,32,3),
            PReLU(),
        )
        self.conv_1 = Conv2d(32,2,1)
        self.conv_2 = Conv2d(32,2,1)
        self.conv_3 = Conv2d(32,2,1)

        for m in self.modules():
            if isinstance(m,Conv2d):
                init.kaiming_normal(m.weight,mode = "fan_out",nonlinearity = "relu")

    def forward(self,x):
        x = self.layers(x)
        x_1 = self.conv_1(x)
        x_2 = self.conv_2(x)
        x_3 = self.conv_3(x)








