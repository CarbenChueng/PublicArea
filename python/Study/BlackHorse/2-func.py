#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 17:57:30 2020

@author: kabun
"""

#像__init__（）这些带____的方法叫魔术方法。__init__（）是在创建对象时自动调用的
# __str__（）是在print的时候自动调用,里面一定要用return

# =============================================================================
# class Cat:
#     def __init__(self):
#         self.type = "美短"
#         self.name = None
#         
#     def eat(self,fish):
#         gg = 20
#         print("猫吃了%d鱼，还有%d哈哈哈哈"%(fish,gg))
#         
#     def __str__(self):
#         return "哈哈"
#         
# Cat1 = Cat()
# # Cat1.clothes = "纯棉"#类里面没有的就等于添加
# Cat1.eat(10)
# print(Cat1)#这是对象的内存地址
# print(Cat1.clothes)
# =============================================================================


# =============================================================================
# class Cat:
#     def __init__(self):
#         self.type = "美短"
#         self.name = None
#         
#     def eat(self):
#         gg = 20
#         print("猫吃了%s鱼，还有%s哈哈哈哈,"
#               "穿了%s的衣服"%(self.type,self.name,self.clothes))
#         
#         
# Cattt = Cat()
# Cattt.name = "大帅"
# Cattt.clothes = "纯棉"#独有属性，访问时候要加self
# Cattt.eat()
# =============================================================================


# =============================================================================
# #调用成员方法，前面加self就可以了
# class Cat:
#     def work(self):
#         self.jump()
#         self.catch()
#         self.bite()
#         
#     def jump(self):
#         print("猫跳起来了")
#         
#     def catch(self):
#         print("猫捉住了老鼠")
#         
#     def bite(self):
#         print("猫咬住了老鼠")
#         
# TangMu = Cat()
# TangMu.work()
# =============================================================================
        
        
# =============================================================================
# class Phone():
#     def __init__(self):
#         self.power = 100
#         
#     def game(self):
#         print("playing game low10")
#         self.power -= 10
#         
#     def music(self):
#         print("listing music low5")
#         self.power -= 5
#         
#     def call(self):
#         print("calling somebody  low5")
#         self.power -= 5  
#     
#     def answer(self):
#         print("having class  low5")
#         self.power -= 5   
#         
#     def charge(self,num):
#         print("charging  up%d"% num)
#         self.power += num
#      
#     def __str__(self):
#         return "当前手机电量是%d"% self.power
#         
# o = Phone()
# o.game()   
# 
# o.call()
# print(o) 
# 
# o.charge(10)     
# print(o)     
#         
# =============================================================================
        
# =============================================================================
#  #封装，私有       
# class Card():
#     def __init__(self,cardname,password):
#         self.card_id = cardname
#         self.__pwd = password
# 
#     def get_pwd(self):
#         return self.__pwd
#     
#     def setpwd(self,pwd):
#         self.__pwd = pwd
#         
#         
# cad = Card("123123123","465745674")
# 
# print(cad.get_pwd(),cad.card_id)
# =============================================================================


# =============================================================================
# #类变量,对面名是不能修改类变量，因为创建出来的对象是独有的，
# 
# class Cat:
#     m_subject = "猫科"#类变量
#     
#     def __init__(self,cardname,password):
#         self.card_id = cardname#实例变量
#         self.__pwd = password
# 
#     def get_pwd(self):
#         return self.__pwd
#     
#     def setpwd(self,pwd):
#         self.__pwd = pwd
#         
#         
# othercat = Cat("123123123","465745674")
# # Cat.m_subject = "犀牛"#可以修改
# othercat.m_subject = "老虎哈哈"#不能修改
# 
# 
# print(Cat.m_subject)  
# print(othercat.get_pwd(),othercat.card_id)
# 
# =============================================================================

        
        
# =============================================================================
# # 类方法：
# # 1：类方法中不允许使用实例变量和实例方法
# # 2:实例方法中允许使用类变量和类方法
# # class Chinese:
# #     m_subject = "中国"#类变量
#     
# #     def __init__(self,cardname,password):
# #         self.card_id = cardname#实例变量
# #         self.pwd = password  
#     
# #     @classmethod#类方法
# #     def ShowCountry(cls):
# #         print("我是中国人")
#     
# #     def Show(self):
# #         # print("话之你乜西人")
# #         print(self.pwd)
# #         print(Chinese.m_subject)
#         # Chinese.ShowCountry()
#         
# # 演示实例方法调用类成员   
# # c1 = Chinese("264823", "李小龙")    
# # c1.Show()
#    
#  
# # 演示类方法调用实例成员
# # class Chinese:
# #     m_subject = "中国"#类变量
#     
# #     def __init__(self,cardname,password):
# #         self.card_id = cardname#实例变量
# #         self.pwd = password  
#     
# #     @classmethod#类方法
# #     def ShowCountry(cls):
# #         print("我是中国人")
# #         # print(self.pwd)  报错
# #         # self.Show()     报错
#     
# #     def Show(self):
# #         # print("话之你乜西人")
# #         print(self.pwd)
# #         print(Chinese.m_subject)
# #         Chinese.ShowCountry()        
# 
# # Chinese.ShowCountry()
# =============================================================================


# =============================================================================
# # 静态方法 实例和类都可以访问
# class Chinese:
#     m_subject = "中国"#类变量
#     
#     def __init__(self,cardname,password):
#         self.card_id = cardname#实例变量
#         self.pwd = password  
#     
#     @staticmethod #静态方法
#     def ShowCountry():
#         print("我是中国人")
#     
# 
# p = Chinese("aaaaaa", "68746582")
# p.ShowCountry()  
# Chinese.ShowCountry()
# =============================================================================
        

# =============================================================================
# # 继承:不能四成父类私有属性
# class Animal:
#     # 父类
#     def __init__(self):
#         self.name = None
#         self.__age = 36
#            
#         
#     def show(self):
#         print("我是一只小老虎")
# class Cat(Animal):
#     pass
# 
# 
# c = Cat()
# # c.__age = 22 报错，因为父类私有
# c.show()
# 
# print(c.age)
# 
# =============================================================================


# =============================================================================
#查看继承的层次结构
# class Person:
#     # def __str__(self):
#     #     return None
#     def fight(self):
#         print("wo shi diyi ")
# class xiaolong():
#     def __init__(self):
#         print("利息哦啊龙牛逼")
#     def fight(self):
#         print("练武，阿打啊打啊打啊打")
#     # def __str__(self):
#     #     return None
    
    
# class haha(xiaolong):
#     def __init__(self):
#         print("我也差不多啊")
#         super().__init__()
#     def fight(self):
#         print("哈哈哈哈啊哈哈")
# # 被重写后依然调用父类的方法
# # 第一种  多继承推荐第一种
#         # xiaolong.fight(self)
        
# # 第二种
#         # super(haha,self).fight()
#         # 
# # 第三种  推荐
#         super().fight()
        
#     def __str__(self): #这是重写object的
#          print(super().__str__())
#          return "我是kabun"
     

# # print(haha.__mro__)#查看继承的层次结构
# p = haha()
# p.fight()

# print(p)

# =============================================================================


# =============================================================================
# #多继承
# class Father():
#     def sing(self):
#         print("唱歌很牛逼")
# 
#     def dance(self):
#         print("跳舞不牛逼")
# 
# class Mother():
#     def sing(self):
#         print("唱歌不不不不不不牛逼")
# 
#     def dance(self):
#         print("跳舞呵呵呵呵呵你牛逼")
#    
#      
# class Child(Father,Mother):
#     def sing(self):
#         print("儿子不会唱歌")
#         Mother.dance(self)
# 
# c= Child()
# c.sing()
# =============================================================================



# =============================================================================
# # 多态：发生在继承关系的基础上
# class Driver:
#     def drive(self):
#         print("开车")
# 
# class Teacher:
#     def teach(self):
#         print("教书")
# 
# 
# class Man(Driver,Teacher):
#     def teach(self):
#         print("这个男人教玩游戏")
# 
#     def drive(self):
#         print("这个男人开马自达")
# 
# class Test:
#     def play(self,ddddd):
#         ddddd.drive()
#         print("阿我只会啪啪啪啪")
#         
#     def study(self,tetete):
#         tetete.teach()
#         print("我想要学习啊啊啊")
# 
# # 方案一：创建司机对象
# d = Driver()
# # 方案二：创建了一个具有司机特征的对象
# ma = Man()
# tt = Test()
# tt.play(ma) #多态形式
# tt.study(ma)  #多态形式
# =============================================================================



# =============================================================================
# # 引用类型参数
# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
# 
# x_name = "哈哈"
# x_age = 16
# 
# p = Person("李小龙", 26)
# 
# def demo(name,age,person):
#     # 修改demo的name,age,person的值（在函数内部修改）
#     x_name = "改了哈哈"
#     x_age = 22
#     person.name = "牛逼李小龙"
#     person.age  =  36
# 
# demo(x_name,x_age,p)#这个p（对象）就等于引用类型的参数，所以会发生改变
# print(x_name,x_age,p.name,p.age)   
# 
# =============================================================================

# ====================================反恐精英=========================================
# 
# # 反恐精英
# # 1:定义人类，描述公共属性 life:100  name:姓名要传参
# # 2:定义出英雄与恐怖分子
# # 3:定义函数描述枪战过程main，创建两个对象
# # 4:定义开枪方法。英雄敌人都有
# #     定义的方法要传入被设计的对象
# #     被射击对象的生命值要进行减少
# # 5:主程序中调用开枪的操作
# # 6:开枪后要显示每个人的状态信息,定义person类的__str__方法。
# # 7:设置开枪操作为反复操作
#     # 有一方生命值<=0  停止循环使用break
# 
# #===========================修复版===========================
# # 9:修复英雄的信息模式
#     # 状态描述 0-70，70-100
# # 10:修复生命显示为负的问题
#     # 射击时，如果生命值<伤害值，=0，就不显示
# #===========================加强版===========================
# # 11:创建三个恐怖分子的对象
#     # 三个对象都要开枪和打印状态
# # 12:修复条件为3个恐怖分子同时满足死亡
# # 13：解决向三个恐怖分子开枪的问题,(random)随机开枪
# #===========================超级加强版===========================
# # 14.加入开枪射击命中率
#     # 产生一个随机数，在范围内就命中，文字效果要有变化
#     
# # 15.加入伤害波动值范围
#     # 产生随机数，加入伤害值
# # 16.加入鞭尸文字显示效果
# 
# 
# 
# import random
# 
# class Person:
#     def __init__(self,name):
#         self.name = name
#         self.life = 100
# 
#     def __str__(self):
#         return "%s的生命值为%d"%(self.name,self.life)
# 
# class Hero(Person):
#     def fire(self,p):
#         
#         # 加入命中率
#         hit_rate = random.randint(1, 100)
#         if hit_rate >= 20:#命中率80%    
#             #判断当前射击的是否是尸体
#             if p.life == 0:
#                 print("%s都已经死了，请停止"% p.name)
#             else:
#                 damage = random.randint(20, 60)#伤害随机
#                 print("%s向%s开枪，造成了%d的伤害"%(self.name,p.name,damage))
#                               
#                 if p.life < damage:
#                     p.life = 0
#                     
#                 else:
#                     p.life -= damage
#             
#          
#         else:
#             print("没有命中")
#        
#         
#     def __str__(self):
#         state = ""
#         if self.life == 100:
#             state = "无伤"
#         elif 70 <= self.life and self.life <= 99:
#             state = "轻伤"
#         elif 1 <= self.life and self.life <= 69:
#             state = "重伤"
#         elif self.life <= 0:
#             state = "死亡"
#         return "%s的生命值为%s"%(self.name,state)
# 
# class Enemy(Person):
#     def fire(self,p):
#         damage = random.randint(3, 8)#伤害随机
#         hit_rate = random.randint(1, 100)
#         if hit_rate >= 70:#命中率30%            
#             print("%s向%s开枪，造成了%d的伤害"%(self.name,p.name,damage))
#                           
#             if p.life < damage:
#                 p.life = 0
#             else:
#                 p.life -= damage
#             
#             
#         else:
#             print("敌人没有命中，像个机器人")
#     
#     def __str__(self):
#         return "%s的生命值为%d"%(self.name,self.life)
# 
# def main():
#     H = Hero("英雄——李小龙")
#     E1 = Enemy("敌人——路人甲")
#     E2 = Enemy("敌人——路人乙")
#     E3 = Enemy("敌人——路人丙")
#     
#     while True:
#         x = random.randint(1, 4)
#         if x==1: 
#             H.fire(E1)
#         elif x==2:
#             H.fire(E2)
#         else:
#             H.fire(E3)
#         E1.fire(H)
#         E2.fire(H)
#         E3.fire(H)
#         
#         print(H,E1,E2,E3)
#         print()
#         if H.life <= 0:
#             print("%s死亡，%s胜利"%(H.name,E1.name))
#             break
#             
#         elif E1.life <= 0 and E2.life <= 0 and E3.life <= 0:
#             print("所有敌人死亡，%s胜利"%H.name)
#             break
#         
#         
# main()
# 
# 
# 
# =============================================================================

 









































