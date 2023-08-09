import numpy as np,torch as tc,os,torch.nn as nn
from PIL import Image,ImageDraw
from _PythonProject._04_YellowPerson.img_data import YelloKidsDataSet
from _PythonProject._04_YellowPerson.Yellow_Net import cnn_net
from torch.utils import data
from torch.backends import mps

De = "mps" if mps.is_available() else "cpu"

save_path = "./model/param_cnn.pt"
if __name__ == '__main__':
    data_set = YelloKidsDataSet("D:\PyCharmProject\AiProject1\YellowPerson\img\dtag")


    net = cnn_net().to(De)
    if os.path.isfile(save_path):
        net = tc.load(save_path)
    loss_func = nn.MSELoss()

    optimizer = tc.optim.Adam(net.parameters())

    # Train = True
    Train = False
    while True:
        if Train:
            train_data = data.DataLoader(dataset=data_set,batch_size=50,shuffle=True)
            for i,(img,tag)in enumerate(train_data):
                img = img.permute(0,3,1,2)
                img = img.to(De)
                out = net(img)
                tag = tag.to(De)
                loss = loss_func(out,tag)

                optimizer.zero_grad()
                loss.backward()
                optimizer.step()
                if i%20==0:
                    print(loss.item())
                    tc.save(net,save_path)

        else:
            train_data = data.DataLoader(dataset=data_set, batch_size=1, shuffle=True)
            for i,(x,y)in enumerate(train_data):
                x = x.permute(0,3,1,2)
                x = x.cuda()
                out = net(x)
                x = x.permute(0,2,3,1)
                x = x.cpu()

                out_put = out.cpu().detach().numpy()*300
                y = y.numpy()*300

                img_data = np.array((x[0]+0.5)*255,dtype=np.int8)
                img = Image.fromarray(img_data,"RGB")

                draw = ImageDraw.Draw(img)
                draw.rectangle(out_put[0],outline="red")#网络输出的结果
                draw.rectangle(y[0],outline="yellow")#网络标签
                img.show()



                
