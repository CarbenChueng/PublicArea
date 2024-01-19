import torch.nn as nn
import torch

class cnn_net(nn.Module):

    def __init__(self):
        super().__init__()
        self.cnn_laters = nn.Sequential(
            nn.Conv2d(3,16,3),
            nn.ReLU(),
            nn.MaxPool2d(2),

            nn.Conv2d(16, 32, 3, 1, 2),
            nn.ReLU(),
            nn.MaxPool2d(2),

            nn.Conv2d(32, 64, 3),
            nn.ReLU(),
            nn.MaxPool2d(2),

            nn.Conv2d(64, 78, 3),
            nn.ReLU(),

            nn.Conv2d(78, 96, 3),
            nn.ReLU(),

            nn.Conv2d(96,128,3),
            nn.ReLU(),
        )

        self.mlp_layer = nn.Sequential(
            nn.Linear(128*30*30,4)
        )

    def forward(self,x):
        cnn_out = self.cnn_laters(x)
        # print(cnn_out.shape)
        cnn_out = cnn_out.reshape(-1,128*30*30)
        out_put = self.mlp_layer(cnn_out)
        return out_put


if __name__ == '__main__':
    net = cnn_net()
    x= torch.randn(6,3,300,300)
    y = net(x)
    print(y.shape)

# class cnn_net(nn.Module):
#
#     def __init__(self):
#         super(cnn_net, self).__init__()
#         self.fc_layers = nn.Sequential(
#             nn.Linear(300*300*3,100),
#             nn.LeakyReLU(),
#             nn.Linear(100,96),
#             nn.LeakyReLU(),
#             nn.Linear(96,78),
#             nn.LeakyReLU(),
#             nn.Linear(78,64),
#             nn.LeakyReLU(),
#             nn.Linear(64,58),
#             nn.LeakyReLU(),
#             nn.Linear(58,52),
#             nn.LeakyReLU(),
#             nn.Linear(52,4),
#         )
#
#     def forward(self,x):
#         return self.fc_layers(x)
#
# if __name__ == '__main__':
#     cnnNet = cnn_net()
#     x = torch.randn(3,300*300*3)
#     y = cnnNet(x)
#     print(y.shape)
