//
//  1_Const.cpp
//  Num_1
//
//  Created by kabun  on 2020/4/18.
//  Copyright © 2020 kabun . All rights reserved.
//

#include <stdio.h>
#include <iostream>
#include <string>
using namespace std;
#define Day 7


 void MultiplicationTable()
 {
    for(int i = 1;i < 10;i++)
    {
        for(int l = 1;l<=i;l++)
            {
                cout << l <<" * "<< i << " = "<< i*l<<"\t";
            }
        cout << endl;
    }
 
 }

int main()
{
    //Day = 14; 不能被修改
    const int Year = 12;
    float f1 = 3.1415;
    double d1 = 6.66666666;
    char ch2 = 'k';//必须只能放一个字母
    //科学计数法
    float f2 = 3e2;//3*10^2
    float f3 = 3e-2;//3*10^-2
    
    string haha = "你玩晒咩";
    
    cout << "一周一共有  " << Day << "天" << endl;
    cout << "一年一共有  " << Year << "年" << endl;
    cout <<  f1 << endl;
    cout <<  d1 << endl;
    cout <<  f2 << endl;
    cout <<  f3 << endl;
    cout <<  int(ch2) << endl;//查看ascii编码
    cout << haha <<endl;
    
    int newha = 0;
    cout << "请输入值" << endl;
    cin >> newha;
    cout << "原来是0，已经改成 "<< newha << endl;
    return 0;
}

