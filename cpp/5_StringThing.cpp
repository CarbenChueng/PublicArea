//
//  5_StringThing.cpp
//  cpp
//
//  Created by kabun  on 2020/4/19.
//  Copyright © 2020 kabun . All rights reserved.
//
#include <stdio.h>
#include <iostream>
#include <string>
#include <ctime>
using namespace std;

#include <stdio.h>

//结构体数组
/*
//========================================================================================================
struct Student
{
    string name;
    int score;
    int age;
};

struct Teacher
{
    string name;
    int age;
    Student stu;
    
};
int main()
{
    Student stuarry[3]=
    {
        {"静静",66,22},
        {"丫丫",88,26},
        {"雯雯",99,28}
    };
    
    stuarry[2].name = "包包";
    stuarry[2].score = 100;
    
    for(int i =0;i<3;i++)
    {
        cout <<"姓名: " <<stuarry[i].name<<"  年龄:  "<<stuarry[i].age <<"  分数:  "<<stuarry[i].score<<endl;
    }
    
    //指针访问结构体的方式
    Student s1 = {"涵涵",100,26};
    Student* p =&s1;
    
    Student*hh = &stuarry[0];
    Teacher t1 = {"张老师",33,s1};
    
    cout << p->name <<p->score<<p->age<<endl;
    cout << hh->name <<hh->score<<hh->age<<endl;
    cout <<t1.stu.name;
    
    return 0;
}
*/
 
//===============================================const在函数中的使用=========================================================
/*
struct Student
{
    string name;
    int score;
    int age;
};

//在函数的形参改为指针，可以减少内存空间，而且不会复制副本出来
void Ps(const Student* ss)
{
    //ss->age = 100; 报错，因为有const所以不能修改
    cout << ss->name << ss->age << ss->score <<endl;
    
}


int main()
{
    Student ss1 = {"你老味",200,300};
    Ps(&ss1);
    //通过函数结打印结构体变量的信息
    
    return 0;
}
 */

//===============================================结构体案例=========================================================
/*
struct Student
{
    string name;
    int age;
    int score;
};

struct Teacher
{
    string name;
    int age;
    Student sarray[5];
    
};

void MTS(struct Teacher tarray[],int len)
{
    //给老师赋值
    string nameseed = "ABCDE";
    for(int i = 0; i<len;i++)
    {
        tarray[i].name = "我的超级老师";
        tarray[i].name += nameseed[i];
        
        for(int l = 0; l<5; l++)
        {
            tarray[i].sarray[l].name = "聪明的学生";
            tarray[i].sarray[l].name += nameseed[l];
            
            int random = rand()% 41+60;
            tarray[i].sarray[l].score = random;
        }
    }
    
}

void PTS(struct Teacher tarray[],int len)
{
    for(int i = 0; i<len;i++)
    {
        cout << "老师的姓名  " << tarray[i].name <<endl;
        for(int l = 0; l<5; l++)
        {
            cout << "\t学生的姓名  " << tarray[i].sarray[l].name
            << "考试分数  " << tarray[i].sarray[l].score <<endl;
        }
    }
}

int main()
{
    //随机数种子
    srand((unsigned int)time(NULL));
    
    Teacher tarray[3];
    int len = sizeof(tarray)/sizeof(tarray[0]);
    
    MTS(tarray, len);
    PTS(tarray, len);
    return 0;
}
*/


//===============================================英雄年龄冒泡排序=========================================================
/*
struct Hero
{
    string name;
    int age;
    string sex;
};

void BubbleSort(struct Hero HArry[],int len)
{
    for(int i = 0; i<len;i++)
    {
        
        for(int l = 0; l<len-i-1; l++)
        {
            if(HArry[l].age >HArry[l+1].age)
            {
                struct Hero temp = HArry[l];
                    HArry[l] = HArry[l+1];
                    HArry[l+1] = temp;
            }
        }
    }
    
}

void PrintHero(struct Hero HArray[],int len)
{
    for(int i = 0; i<len;i++)
    {
        cout << "姓名\t" << HArray[i].name
        << "\t年龄\t" << HArray[i].age
        << "\t性别\t" << HArray[i].sex << endl;
        
    }
}

int main()
{
    struct Hero HArray[5] =
    {
        {"式样",23,"男"},
        {"豆哥",26,"男"},
        {"猪腰",18,"男"},
        {"痴汉博君",22,"男"},
        {"美女",28,"你估下"}
    };
    
    int len = sizeof(HArray)/sizeof(HArray[0]);
    
    cout << "排序前：" << endl;
    for(int i = 0; i<len;i++)
       {
           cout << "姓名\t" << HArray[i].name
                << "\t年龄\t" << HArray[i].age
                << "\t性别\t" << HArray[i].sex << endl;
                
       }
     
    
    BubbleSort(HArray,len);
    cout << "排序后：" << endl;
    PrintHero(HArray,len);
    return 0;
}
*/
