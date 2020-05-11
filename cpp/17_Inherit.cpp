//
//  17_Inherit.cpp
//  cpp
//
//  Created by kabun  on 2020/5/5.
//  Copyright © 2020 kabun . All rights reserved.
//

#include <stdio.h>
#include <iostream>
#include <string>
#include <ctime>
using namespace std;

//===========================================继承==========================================
//class BasePage
//{
//public:
//    void herder()
//    {
//        cout << "帮助中心，交流合作，站内地图" << endl;
//    }
//
//    void buttom()
//    {
//        cout << "Java，python，c++" << endl;
//    }
//
////    void content()
////    {
////        cout << "c++学科视频" << endl;
////    }
//};
////Java页面
//class Java:public BasePage
//{
//public:
//    void content()
//    {
//    cout << "Java学科视频" << endl;
//    }
//};
////Python页面
//class Python:public BasePage
//{
//    public:
//    void content()
//    {
//    cout << "Python学科视频" << endl;
//    }
//
//};
//
//void test()
//{
//    Java j;
//    j.herder();
//    j.content();
//
//    Python p;
//    p.herder();
//    p.content();
//
//}
//int main()
//{
//    test();
//    return 0;
//}

//===========================================继承权限=========================================
//
//class Father
//{
//public:
//    int a = 10;
//protected:
//    int b = 20;
//private:
//    int c = 30;
//};
//
//class Son1 : public Father//=========================公共继承=======================
//{
//public:
//    void test()
//    {
//        cout << a << endl;
//        cout << b << endl;
////        cout << c << endl;//不能访问
//    }
//};
//
//class Son2 : protected Father//=========================保护继承=======================
//{
//public:
//    void test()
//    {
//        cout << a << endl;//父类中的公有成员到子类中变成保护权限（因为是保护继承）
//        cout << b << endl;
////        cout << c << endl;//不能访问
//    }
//};
//
//class Son3 : private Son2//=========================保护继承=======================
//{
//public:
//    void test()
//    {
//        cout << a << endl;//父类中的公有成员到子类中变成保护权限（因为是保护继承）
//        cout << b << endl;
////        cout << c << endl;//不能访问
//    }
//};
//
//class GSon : Son3
//{
//    public:
//    void test()
//    {
////        cout << a << endl;//父类中的成员都是私有权限（因为是私有继承）
////        cout << b << endl;
//    }
//
//};
//
//void test1()
//{
//    //=========================公共继承=======================
////    Son1 s1;
////    s1.test();
////    cout << s1.a << endl;
////    cout << s1.b << endl;//错误，因为是保护权限
//
//    //=========================保护继承=======================
//    Son2 s2;
//    cout << sizeof(s2) << endl;//父类中所有静态的成员属性都会被子类继承下去，其中私有成员是被编译器隐藏了
////    s2.test();
//
////    cout << s2.a << endl;//报错，因为保护权限
////    cout << s1.b << endl;//错误，因为是保护权限
//    //=========================私有和保护一样继承=======================
//}
//
//
//
//int main()
//{
//    test1();
//    return 0;
//}
//
//=========================================继承中的对构造和析构的顺序=======================================
//class f
//{
//public:
//    f()
//    {
//        cout << "构造函数" << endl;
//    }
//
//    ~f()
//    {
//        cout << "析构=-=-=-=-函数" << endl;
//    }
//
//};
//
//class son  : public f
//{
//public:
//    son()
//    {
//        cout << "son;;;;;;构造函数" << endl;
//    }
//
//    ~son()
//    {
//        cout << "son ;;;;;析构=-=-=-=-函数" << endl;
//    }
//};
//
//void haha()
//{
//    //f ff;
//    son s;
//
//}
//
//int main()
//{
//    haha();
//    return 0;
//}


//=========================================继承中，同名成员的处理方式=======================================
//class Father
//{
//public:
//    Father()
//    {
//        aa = 10;
//    }
//
//    void func()
//    {
//        cout  << "这是父类" << endl;
//    }
//
//    void func(int a)
//    {
//        cout  << "父类重载。。这是哈哈哈哈哈类" << endl;
//    }
//
//    int aa;
//};
//
//class Son1 : public Father//=========================公共继承=======================
//{
//public:
//    Son1()
//    {
//        aa = 200;
//    }
//
//    void func()
//    {
//        cout  << "这是哈哈哈哈哈类" << endl;
//    }
//
////    void func(int a)
////    {
////        cout  << "儿子重载。。这是哈哈哈哈哈类" << endl;
////    }
//    int aa;
//};
////继承中 同名成员函数的调用
//void test()
//{
//    Son1 ss;
//    ss.func();
//    ss.Father::func();
//    //如果父类中出现和子类同名的成员函数，子类的同名成员会隐藏掉父类所有的同名成员
//    //如果想访问需要加作用域
//    ss.Father:: func(100);
//
//}
//int main()
//{
//    //继承中，同名成员变量的处理方式
////    Son1 s;
////    cout  << "儿子的事" <<s.aa << endl;
////    cout  << "用儿子访问父类同名的变量" <<s.Father:: aa << endl;
//
//    //继承中，同名成员函数的处理方式
//    test();
//    return 0;
//}

//=======================================静态同名处理方式
//class Base
//{
//public:
//    static int a;
//
//};
//int Base:: a = 10;
//
//class Son : public Base
//{
//public:
//    static int a;
//
//};
//int Son:: a = 200;
////同名静态变量
//void test()
//{
//    Son ss;
//    //通过类名访问
//    cout << ss.a << endl;
//    cout << Son::Base:: a << endl;
//
//}
//
//int main()
//{
//
//    test();
//    return 0;
//}

//=========================================多继承======================================
//
//class Base1
//{
//public:
//    Base1()
//    {
//        a = 100;
//    }
//    int a;
//};
//
//
//class Base2
//{
//public:
//    Base2()
//    {
//        a = 300;
//    }
//    int a;
//};
//class Son : public Base1,public Base2//多继承
//{
//public:
//   Son()
//    {
//        c = 600;
//    }
//    int c;
//};
//void test()
//{
//    Son s;
////    cout << "占用空间" << sizeof(s) <<endl;
//    cout <<  "占用空间" <<s.c <<endl;
//    cout << s.Base1::a <<endl;
//    cout << s.Base2::a <<endl;
//}
//
//int main()
//{
//    test();
//    return 0;
//}

//=========================================菱形继承======================================

class Animal
{
public:
    int m_age = 0;
     
};

//利用虚继承解决菱形继承的资源浪费问题 virtual

//羊
class Sheep: virtual public Animal
{
    
};

//骆驼
class Tuo : virtual public Animal
{
    
};

//羊驼类
class Fuck : public Sheep,public Tuo
{
    
    
};

void test()
{
    Fuck sh;
    sh.Sheep:: m_age = 30;
    sh.Tuo:: m_age = 100;
    //菱形继承也要加作用域，因为父类有相同的数据，
//    cout << sh.Sheep::m_age << endl;
//    cout << sh.Tuo::m_age << endl;
    cout << sh.m_age << endl;
    //菱形继承有有两份数据，资源浪费.原理是指针偏移到一起了，以最后一个为准
    
}

int main()
{
    test();
    return 0;
}




 
