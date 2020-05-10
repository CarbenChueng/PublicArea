//
//  10_Fuction.cpp
//  cpp
//
//  Created by kabun  on 2020/4/21.
//  Copyright © 2020 kabun . All rights reserved.
//

#include <stdio.h>
#include <iostream>
#include <string>
#include <ctime>
using namespace std;

/*
//如果有参数了，那么后面c等等必须要有，前面可以没有。如果c没有会报错
int func(int a,int b = 10, int c = 20)
{
    return a + b+ c;
    
}

//声明和实现只能有一个有默认参数，不然就会产生二意性
//int func2(int b = 10, int c = 20);
//int func2(int b = 20, int c = 10)//会报错
//{
//    return b+ c;
    
//}

//站位参数,可以不给名字，只给数据类型，如果有值，那么调用的时候可以只传一个就可以了。
void func3(int , int)
{
    cout << "hahahahahah" << endl;
}

int main()
{
    func3(10,20);
    return 0;
}
*/

//================================================函数重载===================================================
/*
void func()
{
    cout << "ha调用第一个hahah" << endl;
}

void func(int a)
{
    cout << "hg调用第二个agahah" << endl;
}

void func(int a ,int b)
{
    cout << "调用第三个h" << endl;
}

void func(double b, int a)
{
    cout << "ha调用第四个" << endl;
}

void func(int b, double a)
{
    cout << "ha调用第五个" << endl;
}

int main()
{
    func();
    func(10);
    func(10,20);
    func(3.1213,30);
    
    return 0;
}
 */

/*
//引用作为函数重载的条件
void func(int& a)
{
    cout << "ha调用第一个hahah" << endl;
}

void func(const int& a)
{
    cout << "hg调用第二个agahah" << endl;
}

//函数重载碰到默认参数

void func2(int a)
{
    cout << "ha调用第一个hahah" << endl;
}

void func2(int a,int b = 10)
{
    cout << "hg调用第二个agahah" << endl;
}
int main()
{
    int a = 20;
    //func(a);//会调用第一个
    //func(20);//会调用第二个，因为有const
    
    //函数重载碰到默认参数
    //func2(20);//会报错，因为出现二义性
    
    return 0;
}
*/
