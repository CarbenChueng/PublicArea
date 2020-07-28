#关键字参数必须在无定向实参后面
# 可变参数一定要在位置参数后面

# def haha(c,a = 100,b=29):
#     print(a,b)
# haha(2.1, c= 1)#错误
# haha(b = 2.1, 1)#错误

# def test(a,b,*args):
#     for data in args:
#         print(data)
#
# test(3,2,6,"g","g",)

# print(1,2,3,4,5,sep="\n") #sep 为分隔符
# =========================================================================
# def cece(a,*args,b):
#     print(a,b,args)
#
# cece(1,32,2,3,4,5,6,b = 3)
# =========================================================================
# def test(**kwargs):
#     for i in kwargs.keys():
#         print(i)
#         print(kwargs[i])
# test(aaa =1,bff=2)
# =========================================================================
# 案例一:两端去空格，小写转大写，按照空格切割，同行输出，冒号间隔
# "   hello itcase python   " -> HELLO:ITCAST:PYTHON:

# sentences = "   hello itcase python   "
# sentences = sentences.strip(" ").upper().replace(" ",":")
# print(sentences)

# sentences = "   hello itcase python   "
# def code1(str1,**kwargs):
#     str  = str1.split()
#     for data in str:
#         print(data,**kwargs)
#
# def code2(str2, **kwargs):
#     str1 = str2.strip()
#     str1 = str1.upper()
#     code1(str1,**kwargs)
#
# code2(sentences,end=":")
# =========================================================================
# 案例二
# def call4(d = 10,**kwargs):
#     print("call4 的 d = %d"%d)#都没有了
# def call3(c = 10,**kwargs):
#     print("call4 的 d = %d"%c)#在d中  bcd使用字典参数向后传递
#     call4(**kwargs)
# def call2(b = 10,**kwargs):
#     print("call4 的 d = %d"%b)#在cd中  bcd使用字典参数向后传递
#     call3(**kwargs)
# def call1(a = 10,**kwargs):
#     print("call4 的 d = %d"%a) #在bcd中  bcd使用字典参数向后传递
#     call2(**kwargs)
#
# call1(a = 1,b = 2,c =3,d=1)

# =========================================================================
# #一个星号代表拆包，拆开里面每个元素，字典只拆key
# def test(**kwargs):
#     #效果：print("a"，"b"，"c"，"d")
#     print(*kwargs)   #*kwargs对传递过来的所有字典参数中的key进行现实操作
#       #一个星号代表拆包，拆开里面每个元素，字典只拆key
# test(a = 1,b =2,c = 3, d=4)
# 一个星号代表拆包，拆开里面每个元素，字典只拆key
# list1 = [3,5,6]
# tuple1 = ("a","k","7")
# dict1 = {1:"ah",3:"asd",2 :"23"}
# ste = "jkl"
# print(*ste,*tuple1,*dict1,*list1)
# =========================================================================
#
# def sum(num):
#     if num == 1:
#         return 1
#     return sum(num-1)+num
# print(sum(100)) #函数调用最多1000次 （其实是999，因为内置main函数）

# =================================匿名函数=======================================
#匿名                                 正常
#第一种格式：
# add = lambda a,b : a+b              #def add(a,b):
# c = add(3,5)                            #return a+ b
# print(c)
#
# #第二种格式：
# d = (lambda a,b:a+b)(3,7)
# print(d)


#无参：一定要写（）
# r = (lambda :100)()
# print(r)

#多返回值是不可以的，不支持组包，但是可以变成元组，列表
# f1,f2 = (lambda :(3,4))()
# print(f1,f2)

#无返回值
# x = (lambda : (print("hahah"),print("nini")))()
# print(x)

#数据存储类型
# f4 = (lambda :[a**2 for a in range(6) if a %2 ==0])()
# print(f4)

for i in range(100,10000):
    if (i/100)**3+(i/10%10)**3+(i%10)**3 == i:
        print(i)

for n in range(100,1000):
    c = n/100
    b = n/10%10
    d = n%10
    if c**3 + b**3 +d**3 == n:
        print(n)

