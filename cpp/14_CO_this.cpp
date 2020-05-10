//
//  14_CO_this.cpp
//  cpp
//
//  Created by kabun  on 2020/4/24.
//  Copyright © 2020 kabun . All rights reserved.
//

#include <stdio.h>
#include <iostream>
#include <string>
using namespace std;


/*
class Person
{
public:
    Person(int age)
    {
        this->age = age;
    }
    
    Person& PersonAddAge(Person& p)
    {
        //this指针指向被调用的成员函数所属的对象
        this->age += p.age;
        //this只想p2指针，而*this指向是p2这个对象本体
        return *this;
    }
    int age;
};

//解决名称冲突
void test01()
{
    Person p1(18);
    cout << p1.age << endl;
}

//返回对象本身用*this
void test02()
{
    Person p1(10);
    Person p2(10);
    //链式编程思想
    p2.PersonAddAge(p1).PersonAddAge(p1).PersonAddAge(p1);
    //如果写成Person PersonAddAge(**&**)没有返回引用，就会等于20，因为那是值传递，用自动生成的拷贝构造函数
    //后面的p1都不是同一个东西了
    cout << p2.age << endl;
}
int main()
{
    //test01();
    test02();
    return 0;
}
*/

//=====================================常函数，常对象
//
//class Person
//{
//public:
//    //指针的本质是指针常量，指向不能修改
//    //const Person * const this:
//    //在成员函数后面加const，修饰的是this指向，让指针指向的值也不可以修改
//    void ShowPerson() const
//    {
//        this->m_bb = 100;
//        //m_age = 100;
//        //this = NULL;//this指针不可以修改指向
//    }
//    
//    void func()
//    {
//        
//    }
//    
//    int m_age;
//    mutable int m_bb;//特殊变量，即使在常函数中，野可以修改这个值
//};
//
//void test01()
//{
//    Person p;
//    p.ShowPerson();
//}
//
//void test02()
//{
//    const Person pp;
//    //pp.m_age = 100;//报错
//    pp.m_bb  = 200;
//    
//    pp.ShowPerson();
//    //pp.func();//因为不是常函数
//}
//
//int main()
//{
//    
//    return 0;
//}
