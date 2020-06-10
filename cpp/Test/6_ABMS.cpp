//
//  6_ABMS.cpp
//  cpp
//
//  Created by kabun  on 2020/4/20.
//  Copyright © 2020 kabun . All rights reserved.
//

/*
#include <stdio.h>
#include <iostream>
#include <string>
#include <ctime>
using namespace std;

#define Max 1000

void ShowMenu()
{
    cout<<"============================          "<<endl;
    cout<<"======   "<<"1:添加联系人"<<"   ======"<<endl;
    cout<<"======   "<<"2:删除联系人"<<"   ======"<<endl;
    cout<<"======   "<<"3:修改联系人"<<"   ======"<<endl;
    cout<<"======   "<<"4:查询联系人"<<"   ======"<<endl;
    cout<<"======   "<<"5:显示联系人"<<"   ======"<<endl;
    cout<<"======   "<<"6:清空联系人"<<"   ======"<<endl;
    cout<<"======   "<<"0:  退出   "<<"   ======"<<endl;
    cout<<"============================          "<<endl;
}

struct Person
{
    string name;
    string phone;
    string addr;
    int age;
    int sex;
    
};

struct AddrBooks
{
    //通讯录中保存的联系人的数组
    Person PArray[Max];
    //通讯录中当前记录联系人个数
    int size = 0;
};

//添加
void AddPerson(AddrBooks* abs)
{
    if(abs->size == Max)
    {
        cout<<"满人了，加不了"<<endl;
    }
    else
    {
        //添加姓名
        string name;
        cout<<"请输入姓名："<<endl;
        cin >> name;
        abs->PArray[abs->size].name = name;
        
        //添加电话
        cout<<"请输入电话："<<endl;
        string phone;
        cin >> phone;
        abs->PArray[abs->size].phone = phone;
        
        //添加地址
        cout<<"请输入地址："<<endl;
        string addr;
        cin >> addr;
        abs->PArray[abs->size].addr = addr;
        
        //添加年龄
        cout<<"请输入年龄："<<endl;
        int age = 0;
        cin >> age;
        abs->PArray[abs->size].age = age;
        
        //添加性别
        cout<<"请输入性别："<<endl;
        cout<<"1-----男"<<endl;
        cout<<"2-----女"<<endl;
        int sex = 0;
        
        while (true)
         {
             cin >> sex;
             if(sex ==1 || sex ==2)
             {
                 abs->PArray[abs->size].sex = sex;
                 break;
             }
             else
             {
                 cout<<"输入有误，请重新输入"<<endl;
             }
         }
        
        abs->size++;
        cout<<"添加成功"<<endl;
        
        
        
    }
}

void ShowPerson(AddrBooks* abs)
{
    if(abs->size == 0)
    {
        cout<<"里面无人，查你老味啊"<<endl;
    }
    else
    {
        for(int i = 0; i<abs->size; i++)
        {
            cout <<"姓名："<< abs->PArray[i].name
                <<"\t电话："<< abs->PArray[i].phone
                <<"\t地址："<< abs->PArray[i].addr
                <<"\t年龄："<< abs->PArray[i].age
            <<"\t性别："<< (abs->PArray[i].sex ==1? "男":"女") <<endl;
        }
    }
}

int IsExit(AddrBooks* abs,string name)
{
    for(int i = 0; i<abs->size; i++)
    {
        //判断是否找到人
        if(name == abs->PArray[i].name)
        {
            return i;
        }
    }
    return -1;
}

void DelPerson(AddrBooks* abs)
{
    string name;
    cout<<"请输入你要删除的人的姓名"<<endl;
    cin >> name;
    
    int result = IsExit(abs, name);
    
    if(result != -1)
    {
        for(int i = 0; i<abs->size; i++)
        {
            //数据前移
            abs->PArray[i] =abs->PArray[i+1];
        }
        abs->size--;
        cout<<"删除成功"<<endl;
    }
    else
    {
        cout<<"无呢个人，自己霖霖距"<<endl;
    }
    
}

void FindPerson(AddrBooks* abs)
{
    string name;
    cout<<"请输入你要查找的人的姓名"<<endl;
    cin >> name;
    int result = IsExit(abs, name);
    
    if(result != -1)
    {
        cout <<"姓名："<< abs->PArray[result].name
            <<"\t电话："<< abs->PArray[result].phone
            <<"\t地址："<< abs->PArray[result].addr
            <<"\t年龄："<< abs->PArray[result].age
        <<"\t性别："<< (abs->PArray[result].sex ==1? "男":"女") <<endl;
    }
    else
    {
        cout<<"无呢个人，自己霖霖距"<<endl;
    }
    
}

int main()
{
    //创建通讯录结构体变量
    AddrBooks abs;
    //初始化当前人员个数
    abs.size = 0;
    
    
    int select = 0;
    while (true)
    {
        ShowMenu();
        cout<<"请输入你要选择的功能"<<endl;
        
        cin >> select;
        
        if(select == 0)
        {
            cout<<"欢迎再次使用"<<endl;
            break;
        }
        switch (select)
        {
            case 1://1:添加联系人
                AddPerson(&abs);
                break;
            
            case 2://2:删除联系人
                //DelPerson(&abs);
                break;
            
            case 3://3:修改联系人
                   
                break;
            
            case 4://4:查询联系人
                //FindPerson(&abs);
                break;
                
            case 5://5:显示联系人
                ShowPerson(&abs);
                break;
                
            case 6://6:清空联系人
                   
                break;
                
            case 0://0:  退出
                cout<<"欢迎再次使用"<<endl;
                
                break;
                                
            default:
                cout<<"输入有误，请重新输入"<<endl;
                break;
           }
        
        
    }
   return 0;
    
}
*/
