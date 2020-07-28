"""


isinstance(容器1, 容器2)   #判断类型是否一致



############################################字符串####################################################
如果用 """"""" 来打印，不用 \n 也可以换行


# =====================================公共语法========================================
len(容器)                         长度
max(容器)                         最大值
min(容器)                         最小值
index(数据，开始索引，结束索引)      首次出现的索引
count(数据)                       获取数据的总数


# a = [1,2,3,4,5]
# c = a[::2]#深拷贝
# d = a#浅拷贝

# 公共运算符
# list        +   *   in  not in  ><==(元素大小，个数)
# tuple       +   *   in  not in  ><==(元素大小，个数)
# set                 in  not in  ==(只能判断元素大小完全一样的)
# dict                in  not in

# 如果没有判断，for执行完就执行else

# 推导式：
# ll = [i**2 for i in range(1,30) if i % 2 ==0 and i % 7 ==0]
# jj = ["李小龙" for i in range(1,30) if i % 2 ==0 and i % 7 ==0]
# print(ll)
# print(jj)

# dii = {i:i for i in range(1,6)}
# print(dii)

# dcc = {"haha":"11","zaza":"22"}
# print(dcc.keys())
# dll = {dcc[wx]:wx for wx in dcc.keys()}
# print(dll)

#关键字参数必须在无定向实参后面

sep="oo" sep是分隔符,暂时知道在print()里面用

def test(**kwargs):
    #效果：print("a"，"b"，"c"，"d")
    print(*kwargs)   #*kwargs对传递过来的所有字典参数中的key进行现实操作
    #一个星号代表拆包，拆开里面每个元素，字典只拆key
test(a = 1,b =2,c = 3, d=4)

 #一个星号代表拆包，拆开里面每个元素，字典只拆key
list1 = [3,5,6]
tuple1 = ("a","k","7")
dict1 = {1:"ah",3:"asd",2 :"23"}      
ste = "jkl"
print(*ste,*tuple1,*dict1,*list1)

#函数调用最多1000次 （其实是999，因为内置main函数）
#匿名无参函数：后面一定要写（），，r = (lambda:100)()
函数默认返回none,同一个函数中只能执行一次return，return后面的内容将不再执行
匿名函数可以接收多个返回值（元组组包），使用对应数量的变量接收即可

random.random()是增加0-1之间的其中一个值

可变类型：   列表，集合，字典，对象
不可变类型：  数值，字符串，布尔，元组

"""




  
        
        
        
        
