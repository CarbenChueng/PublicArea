//
//  11_CO_1.cpp
//  cpp
//
//  Created by kabun  on 2020/4/21.
//  Copyright © 2020 kabun . All rights reserved.
//

#include <stdio.h>
#include <iostream>
#include <string>
using namespace std;

//案例一：
/*
const double PI = 3.14;
class Circle
{
//访问权限
//公共
public:
    int r = 0;
    double calculatezc()
    {
        return 2 * PI * r;
    }

};

int main()
{
    //创建圆这个对象
    Circle c1;
    c1.r = 100;
    int a = c1.calculatezc();
    cout << a << endl;
    
    return 0;
}
*/

//案例二：
/*
class Student
{
//访问权限
//公共
public:
    string name;
    int number;
    void Set(string names,int num)
    {
        name = names;
        number = num ;
    }
    void Show()
    {
        cout << name << number << endl;
    }
    
   
};
int main()
{
    //创建圆这个对象
    Student s1;
    s1.name = "zhangsan";
    s1.number =1739127937;
    s1.Show();
    
    s1.Set("静静", 26);
    s1.Show();
    //cout << a << endl;
    
    return 0;
}
*/

/*
//案例三：
class Person
{
//访问权限
//公共
public:
    string name;
protected:
    string car;
private:
    int passwaord;
public:
    void func()
    {
        name = "hahaha";
        car = "bmw";
        passwaord = 1360000;
    }
};

int main()
{
    //实力化一个对象
    Person p1;
    p1.name = "李小龙";
    //p1.car = "奔驰";//报错，因为不是public，类外不能访问
    
    return 0;
}
*/

/*
//成员属性设置为私有
//1:可以自己控制读写权限

//2：检测数据有效性
class Person
{
public:
    //姓名读写
   void setname(string sname)
    {
        name = sname;
    }
    
    string getname()
    {
        return name;
    }
    
    //获取密码
    int passw()
    {
        passwaord = 166;
        return passwaord;
    }
    
    void setlover(string slover)
    {
        lover = slover;
    }
    
private:
    //姓名可读可写
    string name;
    //只读
    int passwaord;
    //只写
    string lover;
    
    
};


int main()
{
    //实力化一个对象
    Person p1;
    p1.setname("李小龙");
    cout << p1.getname() <<endl;
    cout << p1.passw() <<endl;
    
    p1.setlover("小泽爱丽丝");//该数据访问不了
    
    return 0;
}
*/
