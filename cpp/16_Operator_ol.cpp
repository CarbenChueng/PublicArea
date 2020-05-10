//
//  16_Operator_ol.cpp
//  cpp
//
//  Created by kabun  on 2020/5/3.
//  Copyright © 2020 kabun . All rights reserved.
//

#include <stdio.h>
#include <iostream>
#include <string>
#include <ctime>
using namespace std;

//===========================================加号运算符重载==========================================

//class Person
//{
//public:
//    int m_A;
//    int m_B;
//    //通过成员函数重载+号
////    Person operator+(Person& p)
////    {
////        Person temp;
////        temp.m_B = this->m_B + p.m_B;
////        temp.m_A = this->m_A + p.m_A;
////        return temp;
////    }
//};
//
////2:全局函数重载+号
//Person operator+(Person& p1,Person& p2)
//{
//    Person temp;
//    temp.m_B = p1.m_B + p1.m_B;
//    temp.m_A = p2.m_A + p2.m_A;
//    return temp;
//}
////函数重载版本
//
//Person operator+(Person& p1,int num)
//{
//    Person temp;
//    temp.m_B = p1.m_B + num;
//    temp.m_A = p1.m_A + num;
//    return temp;
//}
//
//void test01()
//{
//    Person p1;
//    p1.m_A = 10;
//    p1.m_B = 20;
//
//    Person p2;
//    p2.m_A = 30;
//    p2.m_B = 40;
//
//    //成员函数重载调用的本质
//    //Person p3 = p1.operator+(p2);
//    //全局函数重载调用的本质
//    //Person p3 = operator(p1 + p2);
//    Person p3;
//    p3 = p1+p2;
//    cout << p3.m_B << "\t" << p3.m_A << endl;
//
//    //运算符重载 也可以发生函数重载
//    Person p4 = p1 + 50;
//    cout << p4.m_B << "\t" << p4.m_A << endl;
//
//}
//
//int main()
//{
//    test01();
//    return 0;
//}

//===========================================左移运算符重载==========================================
//class Person
//{
//    friend ostream& operator<<(ostream& cout,Person& p);
//public:
//    Person(int a, int b)
//    {
//        m_A = a;
//        m_B = b;
//    }
//    
//private:
//    int m_A;
//    int m_B;
//};
//
////只能用全局函数重载左移运算符
//ostream& operator<<(ostream& cout,Person& p)//本质：operator <<(cout,p)  简化：cout << p
//{
//    cout << "m_B:: "<< p.m_B <<"\tm_A:: "<< p.m_A <<endl;
//    return cout;
//}
//
//void test()
//{
//    Person p1(2,3);
////    p1.m_B = 20;
////    p1.m_A = 30;
//    cout << p1 <<endl;
//    
//}
//
//int main()
//{
//    test();
//    return 0;
//}
