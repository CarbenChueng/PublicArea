import os, torch, numpy, time
from Yellow_Net import cnn_net
from img_data import YelloKidsDataSet
from torch.nn import *
from torch.utils.data import DataLoader
from torch.backends import mps
from tqdm import tqdm
from PIL import Image, ImageDraw

save_path = "/Users/carbenchueng/Desktop/1-Git/Code/_PythonProject/_04_YellowPerson/model/2.t"
Device = "mps" if mps.is_available() else "cpu"

if __name__ == '__main__':
    data_sat = YelloKidsDataSet("/Users/carbenchueng/Desktop/2-Data/Yellow_Pic/tags")
    net = cnn_net().to(Device)

    if os.path.exists(save_path):
        net.load_state_dict(torch.load(save_path))

    loss_func = MSELoss()

    opt = torch.optim.Adam(net.parameters())
    Train = False

    while True:

        if Train:
            epoch = 0
            train_loader = DataLoader(data_sat, batch_size=113, shuffle=True)
            for i, (x, y) in enumerate(tqdm(train_loader)):
                x = x.permute(0, 3, 1, 2).to(Device)
                y = y.to(Device)
                out = net(x)
                loss = loss_func(out, y)

                opt.zero_grad()
                loss.backward()
                opt.step()

                if i % 100 == 0:
                    print(loss.item())
                torch.save(net.state_dict(), f"./model/{epoch}.t")
                epoch += 1
                # exit()
        #
        #
        else:
            test_loader = DataLoader(data_sat, batch_size=1, shuffle=True)
            for i, (x, y) in enumerate(test_loader):
                # net.eval().to(Device)
                x = x.permute(0, 3, 1, 2).to(Device)
                y = y.numpy() * 300
                out = net(x)
                out = out.cpu().detach().numpy() * 300
                print(out)
                x = x.permute(0, 2, 3, 1).cpu()
                img_data = numpy.array(x[0] * 255, dtype=numpy.int8)
                img = Image.fromarray(img_data, "RGB")
                draw = ImageDraw.Draw(img)
                draw.rectangle(out[0], outline="yellow", width=2)
                draw.rectangle(y[0], outline="red", width=2)
                img.show()
                time.sleep(1)
