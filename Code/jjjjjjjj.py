import json,traceback,os,tqdm

# try:
#     simpdata = []
# os.chdir(r"/Users/kabun/Desktop/3-Data/Celeba/test_zuobiao/")
# hh = os.getcwd()
# print(hh)
# path = os.listdir(r"/Users/kabun/Desktop/3-Data/Celeba/all/handlabel_12")
# path = os.listdir("/Users/kabun/Desktop/3-Data/Celeba/test_face/12")
# os.rmdir(path[0])
# print(path[0].split(".")[0])
# for i in range(len(path)):
#     path.remove(".json")
# print(path)
# # print(hh)

# base_path = "/Users/kabun/Desktop/3-Data/Celeba/test_zuobiao/12"
# for i in range(1):
# # for i in range(2):
#     path1 = "/Users/kabun/Desktop/3-Data/Celeba/sample/24"
#     path2 = os.listdir(base_path)
#     path = os.path.join(base_path,path2[i])
    # print(base_path +path2[i])
    # print(path2)
    # path = os.path.join(path1,path2[i].split(".")[0])
    # path = path+".jpg"
    # print(path)
    # with open(path,"r+",encoding="utf-8") as t:
        # data = json.load(t)
        # data["path"] = path
        # print(data["outputs"]["object"][0]["bndbox"]["xmin"])
        # print(data["outputs"]["object"]["bndbox"]["xmin"])
        # t.seek(0)
        # json.dump(data,t,ensure_ascii=False)
        # t.truncate()

print(os.getcwd())