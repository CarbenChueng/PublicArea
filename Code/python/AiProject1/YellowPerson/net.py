import torch.nn as nn
import torch

class cnn_net(nn.Module):

    def __init__(self):
        super().__init__()
        self.cnn_laters = nn.Sequential(
            nn.Conv2d(
                in_channels=3,
                out_channels=16,
                kernel_size=3,
                stride=1,
                padding=2
            ),
            nn.ReLU(),

            nn.MaxPool2d(kernel_size=2),
            nn.ReLU(),


            nn.MaxPool2d(kernel_size=2),
            nn.ReLU(),
            nn.Conv2d(16, 22, 3, 1, 2),


            nn.MaxPool2d(kernel_size=2),
            nn.ReLU(),
            nn.Conv2d(22, 33, 3, 1, 2),

            nn.Conv2d(33, 46, 3, 1, 2),
            nn.ReLU(),

            nn.Conv2d(46, 56, 3, 1, 2),
            nn.ReLU(),

            nn.Conv2d(56, 68, 3, 1, 2),
            nn.ReLU(),
        )

        self.mlp_layer = nn.Sequential(
            nn.Linear(68*45*45,4)
        )

    def forward(self,x):
        cnn_out = self.cnn_laters(x)
        # print(cnn_out.shape)
        cnn_out = cnn_out.reshape(-1,68*45*45)
        out_put = self.mlp_layer(cnn_out)
        return out_put


if __name__ == '__main__':
    net = cnn_net()
    x= torch.randn(1,3,300,300)
    y = net(x)
    print(y.shape)