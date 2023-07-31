import os,numpy as np,traceback,json,utils
import time

from PIL import Image
from tqdm.gui import tqdm

anno_src = r"/Users/kabun/Desktop/3-Data/Celeba/all"
anno_src_test = r"/Users/kabun/Desktop/3-Data/Celeba/test_zuobiao"
# img_dir = r"/Users/kabun/Desktop/3-Data/Celeba/sample"
# save_path = r"/Users/kabun/Desktop/3-Data/Celeba/test_face"
save_path = r"/Users/kabun/Desktop/3-Data/Celeba/target"
add1 = os.listdir(anno_src)

# print(add1)

for face_size in [12,24,48]:
# for face_size in [48]:
    # print("gen %i image"%face_size)
    positive_image_dir = os.path.join(save_path,str(face_size),"positive")
    negative_image_dir = os.path.join(save_path,str(face_size),"negative")
    part_image_dir = os.path.join(save_path,str(face_size),"part")
    # print(positive_image_dir)

    for dir_path in [positive_image_dir,negative_image_dir,part_image_dir]:
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
    #
    positive_anno_filename = os.path.join(save_path,str(face_size),"positive.txt")
    negative_anno_filename = os.path.join(save_path,str(face_size),"negative.txt")
    part_anno_filename = os.path.join(save_path,str(face_size),"part.txt")
    #
    positive_count = 0
    negative_count = 0
    part_count = 0
#
    try:
        positive_anno_file = open(positive_anno_filename,"w")
        negative_anno_file = open(negative_anno_filename,"w")
        part_anno_file = open(part_anno_filename,"w")
    #
        for i1 in tqdm(range(len(add1))):
        # for i1 in tqdm.tqdm(range(3)):
            add2 = os.path.join(anno_src,add1[i1])
            new_add2 = os.listdir(add2)
            # print(add2)
            # print(new_add2)
            for i2 in range(len(new_add2)):
    #         # for i2 in range(1):
                new_add3 = os.path.join(add2,new_add2[i2])
                with open(new_add3,"r+",encoding="utf-8") as t:
                    data = json.load(t)
                    path = data["path"]
                    print(path)
                    # time.sleep(1)
                    with Image.open(path) as img:
                        img_w,img_h = img.size
                        # print(img_w,img_h)
                        x1 = float(data["outputs"]["object"][0]["bndbox"]["xmin"])
                        y1 = float(data["outputs"]["object"][0]["bndbox"]["ymin"])
                        x2 = float(data["outputs"]["object"][0]["bndbox"]["xmax"])
                        y2 = float(data["outputs"]["object"][0]["bndbox"]["ymax"])
                        # print(x1)
                        w = x2-x1
                        h = y2-y1
                        if max(w,h) <40 or x1<0 or y1<0 or w<0 or h<0:
                            continue

                        boxes = [[x1,y1,x2,y2]]
                        cx = x1+ w/2
                        cy = y1+ h/2

                        #生成正样本，部分样本
                        for _ in range(20):
                            w_ = np.random.randint(-w*0.2,w*0.2)
                            h_ = np.random.randint(-h*0.2,h*0.2)
                            cx_ = cx+w_
                            cy_ = cy+h_

                            side_len = np.random.randint(int(min(w,h)*0.8),np.ceil(1.2*max(w,h)))
                            x1_ = np.max(cx_-side_len/2,0)
                            y1_ = np.max(cy_-side_len/2,0)
                            x2_ = x1_+side_len
                            y2_ = y1_+side_len

                            crop_box = np.array([x1_,y1_,x2_,y2_])
                            offset_x1 = (x1-x1_)/side_len
                            offset_y1 = (y1-y1_)/side_len
                            offset_x2 = (x2-x2_)/side_len
                            offset_y2 = (y2-y2_)/side_len

                            face_crop = img.crop(crop_box)
                            face_resize = face_crop.resize((face_size,face_size),Image.ANTIALIAS)

                            iou = utils.iou(crop_box,np.array(boxes))[0]
                            # print(iou)
                            if iou>0.6:
                                positive_anno_file.write(
                                    "positive/{0}.jpg {1} {2} {3} {4} {5}\n".format(
                                        positive_count,1,round(offset_x1,6),round(offset_y1,6),round(offset_x2,6),round(offset_y2,6)
                                    )
                                )
                                positive_anno_file.flush()
                                face_resize.save(os.path.join(positive_image_dir,"{0}.jpg").format(positive_count))
                                positive_count+=1

                            elif iou >0.4:
                                part_anno_file.write(
                                    "part/{0}.jpg {1} {2} {3} {4} {5}\n".format(
                                        part_count,2,round(offset_x1,6),round(offset_y1,6),round(offset_x2,6),round(offset_x1,2)
                                    )
                                )
                                part_anno_file.flush()
                                face_resize.save(os.path.join(part_image_dir,"{0}.jpg").format(part_count))
                                # print(part_image_dir)
                                part_count+=1
                            #
                            # elif iou <0.29:
                            #     negative_anno_file.write(
                            #         "negative/{0}.jpg {1} 0 0 0 0\n".format(
                            #             negative_count,0
                            #         )
                            #     )
                            #     negative_anno_file.flush()
                            #     face_resize.save(os.path.join(negative_image_dir,"{0}.jpg").format(negative_count))
                            #     negative_count+=1

                        # 生成负样本
                        _boxes = np.array(boxes)
                        for i in range(20):
                            side_len = np.random.randint(face_size, min(img_w, img_h) / 1.5)
                            x_ = np.random.randint(0, img_w - side_len)
                            y_ = np.random.randint(0, img_h - side_len)
                            crop_box = np.array([x_, y_, x_ + side_len, y_ + side_len])

                            if np.max(utils.iou(crop_box, _boxes)) < 0.09:   # 在加IOU进行判断：保留小于0.3的那一部分；原为0.3
                                face_crop = img.crop(crop_box)  # 抠图
                                face_resize = face_crop.resize((face_size, face_size), Image.ANTIALIAS) #ANTIALIAS：平滑,抗锯齿

                                negative_anno_file.write("negative/{0}.jpg {1} 0 0 0 0\n".format(negative_count, 0))
                                negative_anno_file.flush()
                                face_resize.save(os.path.join(negative_image_dir, "{0}.jpg".format(negative_count)))
                                negative_count += 1

    except Exception as e:
        traceback.print_exc()


