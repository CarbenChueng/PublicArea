# stt = "hellloo,李小龙"
# skt = "ahg,fr哈uh,sdf"
# num = "6.66"
# t = skt.ljust(字符串个数,"符号") 左侧加，如果数目没超过字符串的总范围，就不操作
# t = skt.center(16,"@") #两侧都加，如果出现单个，先补右边
# t = stt.zfill(15) #左侧补零
# n = num.zfill(6)
# print(t)
# print(n)

# print(stt.islower()) #判断是否小写，不能有中文
# print(stt.isupper()) #判断是否大写，不能有中文
# print(stt.isprintable()) #判断是否可以打印
#
# print(stt.startswith("龙"))
# print(stt.endswith("龙"))  #还可以判断文件后缀名

# f = stt.upper() #转大写
# f = f.lower() #转小写
# c = skt.title() #单词首字母大写，只要不是英文，其他都会当作分隔符
# v = c.swapcase() #大写转小写，小写转大写
# k = v.capitalize() #字符串首字母大写，其余小写
# print(f)
# print(c)
# print(v)
# print(k)

# skt.strip() 去掉左右两边的占位符
# skt.lstrip() 去掉左两边的占位符
# skt.rstrip() 去掉左两边的占位符


# xxx = "1.jpg"
# if xxx.endswith(".jpg") or xxx.endswith(".png"):
#     print( "这是一张图片")

# str = "hello itcast python"
# s = str.partition("a") #以该字符为基准切割，元组形式返回
# s = str.rpartition("o") #以右边的o为基准切割，，元组形式返回
# s = str.split("t",指定个数(多余的放在一起)) #以所有的t为基准，列表形式返回，并且t会消失
# s = str.splitlines() #以换行符切割数据，列表形式返回
# xin = "❤️"
# s = xin.join("haaha") #把❤️加入到字符串每个字符之间
# print(s)

# str = "hello itcast python"
# # s = str.find("t") #从左到右找返回索引  rfind也是
# # index 找不到会报错，find返回-1
# # s = str.replace("t","!!","替换次数") #从左到右找，把所有都会替换，
# print(s)

# # 加密：：：：：
# str1 = "say goodbye"
# dict1 = "".maketrans("abcdefg","1234567")
# # print(dict1)
# str2 = str1.translate(dict1)
# print(str2)
#
# # 解密：：倒着来
#================================================================================================

# 案例：
db_infos = [
            {"name":"张三丰","gender":1,"nick_name":"三爷","idcard":"11010116373808081017",
             "blood":"b","native":"河北省江丹口"},

            {"name":"张打标","gender":1,"nick_name":"斌爷","idcard":"11010119773808081017",
             "blood":"b","native":"河北省江丹口"}

            ]
#循环列表
for person in db_infos:
    #取出个人信息
    name = person["name"]
    nick_name = person["nick_name"]
    gender = person["gender"]
    blood = person["blood"]
    native = person["native"]
    idcard = person["idcard"]
    #判断是否满足条件
    #只要有一个人不满足，跳过检查下一个
    if not name.startswith("张") :
        continue

    if name.find("斌") == -1 and nick_name.find("斌") == -1 :
        continue

    if gender != 1 :
        continue

    if blood.lower() != "b" :
        continue

    if native.find("河北") == -1 :
        continue

    if int(idcard[6:10]) < 1975 or int(idcard[6:10]) > 1978:
        continue

    #设计字典做对应关系（映射）
    genders = {1:"男",2:"女"}
    print("姓名："+ name,"外号：" +nick_name,"性别："+genders[gender],"血型："+blood,"籍贯:"+native,"身份证："+idcard)



