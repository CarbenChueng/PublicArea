//
//  12_CO_2case.cpp
//  cpp
//
//  Created by kabun  on 2020/4/21.
//  Copyright © 2020 kabun . All rights reserved.
//

#include <stdio.h>
#include <iostream>
#include <string>
#include "Point.hpp"
#include "Circle.hpp"
using namespace std;
/*
//====================================================立方体案例=======================================================
//1:创建立方体类
class Cube
{
//3：设计行为，获取立方体的面积和体积
public:
    //设置长
    void setL(int l)
    {
        clong = l;
    }
    //获取长
    int getL()
    {
        return clong;
    }
    
    //设置宽
    void setW(int w)
    {
        cwide = w;
    }
    //获取宽
    int getW()
    {
        return cwide;
    }
    //设置高
    void setH(int h)
    {
        chigh = h;
    }
    //获取高
    int getH()
    {
        return chigh;
    }
    //获取面积
    int calculaterS()
    {
        return 2*clong*cwide + 2*clong*chigh + 2*cwide*chigh;
    }
    //获取体积
    int calculaterV()
       {
           return clong*cwide*chigh;
       }
    //利用成员函数判断是否相等
    bool IsSameClass(Cube& c)
    {
        if(chigh==c.getH()&&clong==c.getL()&&cwide==c.getW())
        {
            return true;
        }
        else
        {
            return false;
        }
    }
//2:设计属性
private:
    int clong;
    int cwide;
    int chigh;
    
};

//4：分别用全局函数和成员函数，判断两个立方体是否相等

bool isSame(Cube& c1,Cube& c2)
{
    if(c1.getH()==c2.getH()&&c1.getL()==c2.getL()&&c1.getW()==c2.getW())
    {
        return true;
    }
    else
    {
        return false;
    }
    
}

int main()
{
    //创建立方体的对象
    Cube c1;
    c1.setL(10);
    c1.setH(2);
    c1.setW(3);
    
    cout << "面积就是：：" << c1.calculaterS() << endl;
    cout << "体积就是：：" << c1.calculaterV() << endl;
    
    //4：分别用全局函数和成员函数，判断两个立方体是否相等
    //创建第二个立方体
    Cube c2;
    c2.setL(10);
    c2.setH(2);
    c2.setW(6);
    
    bool reasult = isSame(c1, c2);
    if(reasult)
       {
           cout << "相等" << endl;
       }
       else
       {
           cout << "不相等" << endl;
       }
    
    //利用成员函数判断
    reasult = c1.IsSameClass(c2);
    if(reasult)
    {
        cout << "成员相等" << endl;
    }
    else
    {
        cout << "成员不相等" << endl;
    }
}
*/

//====================================================点和圆的关系案例=======================================================
//创建点类
/*
class Point
{
public:
    void setX(int x)
    {
        o_x = x;
    }
    
    int getX()
    {
        return o_x;
    }
    void setY(int y)
    {
        o_y = y;
    }
    
    int getY()
    {
        return o_y;
    }
private:
    int o_x;
    int o_y;
    
};
*/

//创建圆
/*
class Circle
{
public:
    void setR(int r)
    {
        o_r = r;
    }
    
    int getR()
    {
        return o_r;
    }
    void setCenter(Point center)
    {
        o_center = center;
    }
    
    Point getCenter()
    {
        return o_center;
    }
private:
    int o_r;
    //在类中可以让另一个类 作为本类中的成员
    Point o_center;
    
};
*/
 

//判断圆和点的关系
//void IsInCircle(Circle& c,Point& p)
//{
//    //计算两点之间距离的平方
//    int distance =
//    (c.getCenter().getX() - p.getX())*(c.getCenter().getX() - p.getX()) +
//    (c.getCenter().getY() - p.getY())*(c.getCenter().getY() - p.getY());
//    //计算半径的平方
//    int rdintance = c.getR()*c.getR();
//
//    //判断关系
//    if(distance == rdintance)
//    {
//        cout <<"点在原上"<< endl;
//    }
//    else if (distance > rdintance)
//    {
//        cout <<"在圆外"<< endl;
//    }
//    else
//    {
//        cout <<"在圆内"<< endl;
//    }
//
//}
//
//
//int main()
//{
//    //创建一个圆
//    Circle c;
//    c.setR(10);
//    Point center;
//    center.setX(10);
//    center.setY(0);
//    c.setCenter(center);
//    //创建一个点
//    Point p;
//    p.setX(10);
//    p.setY(9);
//
//    //判断关系
//    IsInCircle(c, p);
//    return 0;
//}
//

//==========================================类内更改私有属性==========================================
//
//class bb
//{
//
//public:
//    string name;
//    int age;
//    void func()
//    {
//        cout << "咩有const" <<  name <<  age << endl;
//    }
//
//    void setni(string name,int age)
//    {
//         m_age = age;
//         m_name = name;
//    }
//
//    string getname()
//    {
//        return m_name;
//    }
//
//    int getage()
//    {
//        return m_age;
//    }
//
//private:
//    string m_name;
//    int m_age;
//};
//
//
//int main()
//{
//    int b = 10;
//    bb b1;
//    b1.setni("李小龙", 26);
//    b1.func();
//
//    return 0;
//}
