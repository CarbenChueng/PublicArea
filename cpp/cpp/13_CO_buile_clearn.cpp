//
//  13_CO_buile_clearn.cpp
//  cpp
//
//  Created by kabun  on 2020/4/22.
//  Copyright © 2020 kabun . All rights reserved.
//

#include <stdio.h>
#include <iostream>
#include <string>
using namespace std;

////对象初始化和清理
/*
class Person
{
    //构造函数进行初始化：
    //1：没有返回值，也不用写void
    //2：函数名称与类名相同
    //3：构造有参数，可以发生重载。
    //4：构造：程序在调用对象时候会自动调用构造，只会调用一次。
public:
    Person()
    {
        cout << "Person 构造函数的调用" << endl;
    }
    
    //析构函数进行清理
    //1：没有返回值，也不用写void
    //2：函数名称与类名相同（名称前加～）
    //3：没有参数，不可以发生重载。
    //4：程序在销毁前会自动调用构造，只会调用一次。
    ~Person()
    {
        cout << "Person 析构函数的调用" << endl;
    }
    
};
//构造和析构都是必须有的实现，如果自己不提供，编译器会提供一个空实现的构造和析构
void test()
{
    Person p;//在栈上的数据，执行完毕后会自动释放
}

int main()
{
    //test();
    //Person p;//如果这下面有暂停的话，析构是不会出现的，因为没有执行完，不会释放，所以～person就不会执行
    int a = 10;
    
    cout << (a>20) <<endl;
    return 0;
}
*/

//================================================构造函数的调用和分类===================================================
/*
class Person
{
public:
    //无参
    Person()
    {
        cout << "Person 构造函数的调用" << endl;
    }
    //有参
    Person(int a)
    {
        age = a;
        cout << "Person 有参构造函数的调用" << endl;
    }
    //拷贝构造函数
    Person(const Person& w)
    {
        //将传入的人身上的所有属性拷贝到自己身上
        age = w.age;
        cout << "Person 拷贝构造函数的调用" << endl;
    }
    
    ~Person()
       {
           cout << "Person 析构函数的调用" << endl;
       }
    int age = 0;
};

void test()
{
    //括号法。推荐括号法
    //Person p1;//默认构造
    //Person p2(10);//有参构造
    //Person p3(p2);//拷贝构造
    //cout << p2.age << endl;
    //cout << p3.age << endl;
    //(注意：调用默认构造时候不要加(),因为这样编译器会认为是一个函数的声明)
    
    //显示法
    //Person p1;
    //Person p2 = Person(10);//有参
    //Person p3 = Person(p2);//拷贝
    //Person(10) 为匿名构造函数，执行后会被释放
    //cout << "aaaaa" <<endl;
    //(注意：不要利用拷贝函数初始化匿名对象,下面会被编译器认为 Person p3;跟上面的一样了)
    //Person(p3);
    
    //隐式转换法
    Person p4 = 10; //相当于Person(10);
    Person p5 = p4;//拷贝构造
}
    
int main()
{
    test();
    return 0;
}
*/

//拷贝构造函数的调用时机
/*
class Person
{
public:
    
    Person()
    {
        cout << "Person 构造函数的调用" << endl;
    }
    Person(int a)
    {
        num = a;
        cout << "Person 有参构造函数的调用" << endl;
    }
    Person(const Person& p1)
    {
        num = p1.num;
        cout << "Person 拷贝构造函数的调用" << endl;
    }
    
    ~Person()
    {
        cout << "Person 析构函数的调用" << endl;
    }
    int num = 0;
};
//1:使用一个已经创建完毕的对象来初始化一个新对象
void test01()
{
    Person p1(20);
    Person p2(p1);
}
 //2:值传递的方式给函数参数传值
void dowork(Person p)
{
    
}
void test02()
{
    Person p1;
    dowork(p1);
}
//3；以值的方式返回局部对象
Person dowork3()
{
    Person p3;
    cout <<(int*)& p3 <<endl;
    return p3;
}
void test03()
{
    Person p = dowork3();
    cout <<(int*)& p <<endl;
}
int main()
{
    //1:使用一个已经创建完毕的对象来初始化一个新对象
    //test01();
    //2:值传递的方式给函数参数传值
    //test02();
    //3；以值的方式返回局部对象
    test03();
    return 0;
}
*/

//构造函数的调用规则
//默认情况下，c++编译器至少给一个类添加3个函数
//1:默认构造（无参，函数体为空）
//2:默认析构（无参，函数体为空）
//3:默认拷贝构造，对属性进行值拷贝

//调用规则
//1:如果用户定义有参构造函数。c++不再提供默认无参构造，但是会提供默认拷贝构造
//2:如果用户定义拷贝构造函数，c++不再提供其他构造函数
/*
class HAHA
{
public:
    HAHA()
    {
        cout << "haha 默认构造函数的调用" << endl;
    }
    
    HAHA(int a)
    {
        num = a;
        cout << "haha有参构造函数的调用" << endl;
    }
    
    //HAHA(const HAHA& ha)
    //{
    //    num = ha.num;
    //    cout << "haha拷贝构造函数的调用" << endl;
    //}
    
    ~HAHA()
    {
        cout << "Person 析构函数的调用" << endl;
    }
    
    
    int num = 0;
};

void test01()
{
    HAHA p1;
    p1.num = 18;
    
    HAHA h1(p1);
    cout << "Person 析构函数的调用" << h1.num << endl;
}

int main()
{
    test01();
    return 0;
}
*/

//================================================深拷贝和浅拷贝==================================================
/*
class Person
{
public:
    
    Person()
    {
        cout << "Person 构造函数的调用" << endl;
    }
    Person(int a,int high)
    {
        num = a;
        hihihi = new int(high);
        cout << "Person 有参构造函数的调用" << endl;
    }
    //自己实现拷贝构造函数。解决浅拷贝带来的问题
    Person(const Person& ps)
    {
        num = ps.num;
        hihihi = new int(*ps.hihihi);
        cout << "Person 拷贝构造函数的调用" << endl;
    }
    
    ~Person()
    {
        //析构函数通常将堆区开辟的数据释放操作
        if(hihihi != NULL)
        {
            delete hihihi;
            hihihi = NULL;
        }
        cout << "Person 析构函数的调用" << endl;
    }
    int num = 0;
    int* hihihi;
};

void test01()
{
    Person p1(11,170);
    cout << p1.num << *p1.hihihi << endl;
    Person p2(p1);
    cout << p2.num << *p2.hihihi  <<endl;
}

int main()
{
    test01();
    return 0;
}
*/
