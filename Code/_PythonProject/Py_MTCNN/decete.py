import torch,numpy as np,net,time,os,utils
from PIL import Image,ImageDraw
from torchvision import transforms

p_cls =0.6
p_nms =0.2
r_cls =0.6
r_nms =0.5
o_cls =0.3
o_nms =0.5

class Detector:
    def __init__(self,pnet_param = "./param/pnet.pt",rnet_param = "./param/rnet.pt",
                 onet_param = "./param/onet.pt"):
    # def __init__(self,pnet_param = "./param/pnet.pt"):
        self.pnet = net.PNet()
        self.rnet = net.RNet()
        self.onet = net.ONet()

        self.pnet.load_state_dict(torch.load(pnet_param))
        self.rnet.load_state_dict(torch.load(rnet_param))
        self.onet.load_state_dict(torch.load(onet_param))

        self.pnet.eval()
        self.rnet.eval()
        self.onet.eval()

        self.__image_transform = transforms.Compose([
            transforms.ToTensor()
        ])

    def detect(self,image):
        start_time = time.time()
        pnet_boxes = self.__pnet_detect(image)
        if pnet_boxes.shape[0] ==0:
            return np.array([])
        end_time = time.time()
        t_pnet = end_time-start_time

        start_time = time.time()
        rnet_boxes = self.__rnet_detect(image,pnet_boxes)
        if rnet_boxes.shape[0] ==0:
            return np.array([])
        end_time = time.time()
        t_rnet = end_time-start_time

        start_time = time.time()
        onet_boxes = self.__onet_detect(image,rnet_boxes)
        if pnet_boxes.shape[0] ==0:
            return np.array([])
        end_time = time.time()
        t_onet = end_time-start_time

        t_sum = t_pnet+t_rnet+t_onet
        print("total:{0} pnet:{1} rnet:{2} onet{3}".format(t_sum,t_pnet,t_rnet,t_onet))
        return onet_boxes

    def __pnet_detect(self,image):
        boxes = []
        img = image
        w,h = img.size
        min_side_len = min(w,h)

        scale = 1
        while min_side_len >12:
            img_data = self.__image_transform(img)
            img_data.unsqueeze_(0)
            _cls,_offset = self.pnet(img_data)

            cls = _cls[0][0].cpu().data
            offset = _offset[0].cpu().data
            idxs = torch.nonzero(torch.gt(cls,p_cls))

            for idx in idxs:
                boxes.append(self.__box(idx,offset,cls[idx[0],idx[1]],scale))
            scale = 0.7
            _w = int(w*scale)
            _h = int(h*scale)
            img = img.resize((_w,_h))
            min_side_len = min(_w,_h)

        return utils.nms(np.array(boxes),p_nms)

    def __box(self,start_index,offset,cls,scale,stride = 2,side_len = 12):
        _x1 = (start_index[1].float() * stride)/scale
        _y1 = (start_index[0].float() * stride)/scale
        _x2 = (start_index[1].float() * stride + side_len -1)/scale
        _y2 = (start_index[0].float() * stride + side_len -1)/scale

        ow = _x2-_x1
        oh = _y2-_y1

        _offset = offset[:,start_index[0],start_index[1]]
        x1 = _x1 + ow * _offset[0]
        y1 = _y1 + oh * _offset[1]
        x2 = _x2 + ow * _offset[2]
        y2 = _y2 + oh * _offset[3]
        return [x1,x2,y1,y2,cls]

    def __rnet_detect(self,image,pnet_boxes):
        _img_dataset = []
        _pnet_boxes = utils.convert_to_square(pnet_boxes)
        for _box in _pnet_boxes:
            _x1 = int(_box[0])
            _y1 = int(_box[1])
            _x2 = int(_box[2])
            _y2 = int(_box[3])

            img = image.crop((_x1,_y1,_x2,_y2))
            img = img.resize((24,24))
            img_data = self.__image_transform(img)
            _img_dataset.append(img_data)
        img_dataset = torch.stack(_img_dataset)
        _cls,_offset = self.rnet(img_dataset)
        cls = _cls.cpu().data.numpy()
        offset = _offset.cpu().data.numpy()
        boxes = []
        idxs,_ = np.where(cls>_cls)
        for idx in idxs:
            _box = _pnet_boxes[idx]
            _x1 = int(_box[0])
            _y1 = int(_box[1])
            _x2 = int(_box[2])
            _y2 = int(_box[3])

            ow = _x2-_x1
            oh = _y2-_y1
            x1 = _x1+ow*offset[idx][0]
            y1 = _x2+oh*offset[idx][1]
            x2 = _y1+ow*offset[idx][2]
            y2 = _y2+oh*offset[idx][3]
            boxes.append([x1,y1,x2,y2,cls[idx][0]])

        return utils.nms(np.array(boxes),r_nms)


    def __onet_detect(self,image,rnet_boxes):
        _img_dataset = []
        _pnet_boxes = utils.convert_to_square(rnet_boxes)
        for _box in _pnet_boxes:
            _x1 = int(_box[0])
            _y1 = int(_box[1])
            _x2 = int(_box[2])
            _y2 = int(_box[3])

            img = image.crop((_x1,_y1,_x2,_y2))
            img = img.resize((48,48))
            img_data = self.__image_transform(img)
            _img_dataset.append(img_data)
        img_dataset = torch.stack(_img_dataset)
        _cls,_offset = self.rnet(img_dataset)
        cls = _cls.cpu().data.numpy()
        offset = _offset.cpu().data.numpy()
        boxes = []
        idxs,_ = np.where(cls>_cls)
        for idx in idxs:
            _box = _pnet_boxes[idx]
            _x1 = int(_box[0])
            _y1 = int(_box[1])
            _x2 = int(_box[2])
            _y2 = int(_box[3])

            ow = _x2-_x1
            oh = _y2-_y1
            x1 = _x1+ow*offset[idx][0]
            y1 = _x2+oh*offset[idx][1]
            x2 = _y1+ow*offset[idx][2]
            y2 = _y2+oh*offset[idx][3]
            boxes.append([x1,y1,x2,y2,cls[idx][0]])

        return utils.nms(np.array(boxes),o_nms,isMin=True)

if __name__ == '__main__':
    image_path = r"/Users/kabun/Desktop/test_img"
    for i in os.listdir(image_path):
        # print(i)
        detector = Detector()
        with Image.open(os.path.join(image_path,i)) as im:
            print(im.format)
    # with Image.open(image_path) as im:
            print("-"*20)
            boxes = detector.detect(im)
            print("size",im.size)
            imDraw = ImageDraw.Draw(im)
            for box in boxes:
                x1 = int(box[0])
                y1 = int(box[1])
                x2 = int(box[2])
                y2 = int(box[3])
                print("conf :",box[4])
                imDraw.rectangle((x1,y2,x2,y2),outline="red")
            im.show()





    # a = np.arange(24).reshape(4,6)
    # np.save("./param/arrA.npy",a)
    # b = np.load("arrA.npy")
    # print(b)






