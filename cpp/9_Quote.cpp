//
//  9_Quote.cpp
//  cpp
//
//  Created by kabun  on 2020/4/20.
//  Copyright © 2020 kabun . All rights reserved.
//

#include <stdio.h>
#include <iostream>
#include <string>
#include <ctime>
using namespace std;

/*
void test()
{
    int a =10;
    int &b =a;
    int c =20;
    
    b = c;
    
    cout <<a <<endl;
    cout <<b <<endl;
    cout <<c <<endl;
    
}


void swap(int& a,int& b)
{
    int temp = a;
    a = b;
    b = temp;
    
    
    
}

//变成静态变量。就可以返回了
int& test03()
{
    static int a = 10;
    return a;
}

int main()
{
    int a = 10;
    int b = 20;
    //test();
    //swap(a,b);
    int& haha = test03();
    cout <<haha <<endl;
    cout <<haha <<endl;
    cout <<haha <<endl;
    test03() = 200;
    //haha = 300;也可以修改
    cout <<haha <<endl;
    cout <<haha <<endl;
        
    return 0;
}
*/

/*
void show(const int& val)
{
    //val = 200; 加了const会报错，因为不能被修改
    cout << val << endl;
}
int main()
{
    //const int& j = 10;
    //j = 30; 这是错误的
    int a = 100;
    
    show(a);
    cout << a << endl;
    
}
*/
