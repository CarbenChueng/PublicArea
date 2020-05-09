//
//  2_perator.cpp
//  Num_1
//
//  Created by kabun  on 2020/4/18.
//  Copyright © 2020 kabun . All rights reserved.
//

/*
#include <iostream>
#include <string>
#include <ctime>
using namespace std;

// !  &&  ||
void Ornot()
{
    int a = 10;
    int b = 20;
    cout <<(!a)<<endl;
    cout <<(a&&b)<<endl;
    cout <<(a||b)<<endl;
    
}

//if
void Heaviest()
{
    int a = 0;
    int b = 0;
    int c = 0;
    cout << "请输入A小猪的体重" << endl;
    cin >> a;
    cout << "请输入B小猪的体重" << endl;
    cin >> b;
    cout << "请输入C小猪的体重" << endl;
    cin >> c;
    
    if (a > b && a > c )
    {
        cout << "小猪A最重：" <<a << endl;
    }
    else if (a < b || a < c)
    {
        if( b>c)
        {
            cout << "小猪B最重：" << b << endl;
        }
        else
            cout << "小猪C最重：" << c << endl;
    }
    
}

//三目运算
void Bigger()
{
    int a = 10;
    int b = 20;
    int c = 0;
    
    c = a > b ? a:b;
    cout << c << endl;
    
    (a > b ? a:b)=100;
    cout << "a =  " << a << endl;
    cout << "b =  " << b << endl;
}
 
//三目运算-2
void sum()
{
    
    bool b = true;
    string c = b? "true":"false";
    cout << c << endl;
    
}

//switch
void Choose()
{
    int Score = 0;
    cout << "请输入分数(0-10)" << endl;
    cin >> Score;
    
    switch (Score)
    {
        case 10:
            cout << "你觉得很棒" << endl;
            break;
        case 9:
            cout << "你觉得不错" << endl;
            break;
        case 8:
            cout << "你觉得还行" << endl;
            break;
        case 7:
            cout << "你觉得中规中矩" << endl;
            break;
        case 6:
            cout << "你觉得66666" << endl;
            break;
        default:
            cout << "你觉得不行" << endl;
            break;
    }
}

//随机猜数字 rand()%
void RandomNumber()
{
    srand((unsigned int)time(NULL));
    int Num = 0;
    int Rnum = rand()%100+1;
    cout << Rnum << endl;
    cout << "请输入你要猜的数字" << endl;
   
    
    while (true)
    {
        
        cin >> Num;
        if(Num > Rnum)
        {
            cout << "你输入的数字大了" << endl;
        }
        else if (Num < Rnum)
        {
            cout << "你输入的数字小了" << endl;
            
        }
        else
        {
            cout << "你猜对了" << endl;
            break;
        }
    }

}

//水仙花数 do while
void Flower()
{
    int i =100;
    do
    {
        int a = 0;
        int b = 0;
        int c = 0;
        
        a = i%10;
        b = i/10%10;
        c = i/100;
        
        if(a*a*a+b*b*b+c*c*c == i)
        {
            cout << i <<endl;
        }
        
        i++;
    }
    while (i<1000);
        
    
}

//敲桌子 for
void KnockDesk()
{
    for(int i = 1; i<=100;i++)
    {
        if(i%7==0 || i%10==7 || i/10==7)
        {
            cout << "敲桌子" << endl;
        }
        else
            cout << i << endl;
    }
    
}

//continue
void Nc()
{
    for(int l = 0; l<=50; l++)
    {
        if(l%2 == 0)
        {
            continue;
        }
    cout << l <<endl;
    }
}

//goto
void Gothere()
{
    cout << "1----------" << endl;
    goto haha;
    cout << "2----------" << endl;
    cout << "3----------" << endl;
    cout << "4----------" << endl;
    haha:
    cout << "5----------" << endl;
    cout << "6----------" << endl;
    
    
}

//for循环的特别写法
void ForSpecial()
{
    int arr[] = {1,2,3,4,5,6};
    for(int& all : arr)
    {
        cout << all << endl;
    }
    
}
int main()
{
    
    //Ornot();
    //Heaviest();
    //Bigger();
    //Choose();
    //RandomNumber();
    //Flower();
    //KnockDesk();
    //Nc();
    //Gothere();
    //ForSpecial();
    //sum();
}

*/

