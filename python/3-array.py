#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  4 16:00:43 2020

@author: kabun
"""

# ======================================元组=======================================

# # 元祖只有一个元素记得加逗号，不能增删改查
# # class User:
# #     def __init__(self,name,ahe):
# #         self.name = name
# #         self.age = ahe
#         
# #     def __str__(self):
# #         return "姓名是%s：  年龄是:%d"%(self.name,self.age)
# 
# # # u = User()
# 
# # tu = ("哈哈",26,User("李小龙",23),User("周星驰", 36))
# # for i in tu:
# #     print(i)
#     
# # tu[2].age = 33#元组中数据如果是引用类对象，那么它的对象不允许被替换，但是属性值可以发生改变
# # for i in tu:
# #     print(i)
# =============================================================================
    
# ======================================集合=======================================

# # 无序，不能进行索引操作(因为会自动排列)。过滤重复数据
#     
# seee = {True,4,2,False,0,5,1,3}
# print(seee)
# 
# for _ in seee:#如果写的是 下划线 其他人就知道这个是没意义的数据
#     print(_)
# =============================================================================

# =============================================================================
# list
# 增：append,insert(索引，数据) extend(序列名)
# 删：pop(索引) clear()清空所有
# 查：index(数据)，count(数据)  count是查看出现次数
# 
# tuple
# 查：index(数据，开始，结束)，count(数据)是查看出现次数
# 
# set
# 增：add(数据)
# 删：remove（数据），
# pop()删除集合中的第一个数据并得到它
# clear()清空所有
# 
# dict(iterable, kwargs)
# 删 
# pop(键)          指定删除对应的值
# popitem()       删除最后一个添加的键值对
# clear()         清除所有
# 
# 改
# setdefault(键，值)  如果没有就添加    
# update（字典）  如果没有就添加 
# 
# 查
# get()           不存在返回none     dict[key] 会报错
# keys()          获取所有键
# vaules()        获取所有值
# items()         元组方式返回所有键值对
# =============================================================================



# =============================================================================
# list1 = [1,2,3,4,5]
# list2 = ["hahaa","ajhsdkjah","huhuhu",4,5]
# list3 = [6,7,8,9,10]
# list4 = [list1,list2,list3]
# for i in list4:
#     for a in i:
#         print(a)
#     print("======")
#     # print(i)
# 
# print(isinstance(list1, list))   #判断类型是否一致
# =============================================================================


# ======================================斗地主=======================================

# 1:扑克牌对象
# 2:创建发牌堆的列表
# 3:三个玩家额排队列表
# 4:底牌元组
# 5:原始牌堆的初始化，54张牌加入到牌堆
# 6:创建洗牌操作
# 7:创建发牌操作
import random

class Poke:
    pokes = []
    player1 = []
    player2 = []
    player3 = []
    bottom_card = []
    
    def __init__(self,flower,num):
        self.flower = flower  #花色
        self.num = num #大小

    def __str__(self):
        return "%s%s"%(self.flower,self.num)

   
    #初始化牌
    @classmethod
    def InitPoke(cls):
        flowers = ("♠️","♥️","♣️","♦️")
        nums = ("2","3","4","5","6","7","8","9","10","J","Q","K","A")
        kings = {"big":"大王" , "small":"小王"}
        for flower_ in flowers:
            for num_ in nums:
                p = Poke(flower_,num_)
                cls.pokes.append(p)

        cls.pokes.append(Poke(kings["big"],"0"))
        cls.pokes.append(Poke(kings["small"],"0"))
        
    @classmethod
    def Show(cls): 
        for poke in cls.pokes:
            print(poke,end = " ")
        print()
            
    
    
    #洗牌:从牌堆中找出一张固定的牌，与随机的一张交换位置
    @classmethod
    def Wash(cls):
        #迭代牌堆
        #产生随机数，交换
        for idx in range(54):
            
            idxx = random.randint(0, 53)
            cls.pokes[idxx],cls.pokes[idx] = cls.pokes[idx],cls.pokes[idxx]
            
               
    #发牌    
    @classmethod
    def SendPoke(cls):
        for _ in range(0, 17):
            cls.player1.append(cls.pokes.pop(0))
            cls.player2.append(cls.pokes.pop(0))
            cls.player3.append(cls.pokes.pop(0))
            
            #把剩余的3张牌做成底牌
        cls.bottom_card = tuple(cls.pokes)
        
  
    #看三个玩家的牌
    @classmethod
    def ShowPlayers(cls):
        
        print("玩家一：：",end = "")
        for poke in cls.player1:
            print(poke,end = " ")
        print()
        
        print("玩家二：：",end = "")
        for poke in cls.player2:
            print(poke,end = " ")
        print()
        
        print("玩家三：：",end = "") 
        for poke in cls.player3:
            print(poke,end = " ")
        print()
        
        print("底牌：：",end = "") 
        for poke in cls.bottom_card:
            print(poke,end = " ")
        print()
        
        
Poke.InitPoke()
Poke.Show()
Poke.Wash()   
Poke.Show()    
Poke.SendPoke()
Poke.ShowPlayers()