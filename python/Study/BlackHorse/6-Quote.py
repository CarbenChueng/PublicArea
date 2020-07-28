# print(id(-2-2),id(-4))
# print(id(-3-3),id(-6))

#只有空的元组的地址才会一样，
#类的话，没引用会反复回收。

# 可变类型：
# 列表
# 集合
# 字典
# 对象

# 不可变类型：
# 数值
# 字符串
# 布尔
# 元组

# 函数里，如果传的实惨是不可变类型，那么函数内部操作不会对外部产生影响
a = []
b = []
print(id(a),id(b))
a.append(1)
a.append(5)
a.append(4)
a.append(3)
a.append(2)
print(id(a))