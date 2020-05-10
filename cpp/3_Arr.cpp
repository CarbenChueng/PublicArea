//
//  3_Arr.cpp
//  cpp
//
//  Created by kabun  on 2020/4/19.
//  Copyright © 2020 kabun . All rights reserved.
//

#include <iostream>
#include <string>
#include <ctime>
using namespace std;
/*
//获取数组元素地址
void Build()
{
    int arr[] = {1,2,3};

    cout << sizeof(arr) <<endl;
    cout << arr << endl;
    cout << &arr[1] << endl;
}

//找出最大值
void GetBiggest()
{
    int max = 0;
    int arr[] = {2,33,15,66,10};
    for(int i = 0; i<6;i++)
    {
        if(arr[i]>max)
        {
            max = arr[i];
        }
    }
    cout<< max <<endl;
    
}

//元素逆置：倒序
void ReverseOrder()
{
    int arr []={1,2,3,4,5,6};
    int start = 0;
    int end = sizeof(arr)/sizeof(arr[0])-1;
    
    while(start<end)
    {
        
        int temp = arr[start];
        arr[start] = arr[end];
        arr[end] = temp;
        
        start++;
        end--;
    }
    for(int a = 0;a<6;a++)
    {
        cout << arr[a] <<"  ";
    }
}

//冒泡排序
void Bubble()
{
    int arr[] = {8,7,6,5,4,3,2,1};
    int len = sizeof(arr)/sizeof(arr[0]);
    for(int i = 0;i<len-1;i++)
    {
        for(int l = 0;l<len-i-1;l++)
        {
            if(arr[l]>arr[l+1])
            {
                int temp = arr[l];
                arr[l] = arr[l+1];
                arr[l+1] = temp;
            }
            
        }
    }
    for(int a = 0;a<len;a++)
    {
        cout << arr[a] <<"  ";
    }
    
}

//求列，行,每行加起来的总数
void sunmm()
{
    int arr[2][3] =
    {
        {1,2,3},
        {4,5,6}
    };
    string name[] = {"静静","洋洋"};
    for(int i = 0;i<2;i++)
    {
        int sum = 0;
        for(int l = 0; l<3;l++)
        {
            
            sum+= arr[i][l];
        }
        cout << name[i]<<"的个人的总分是"<<sum<<endl;
    }
    cout <<"改数组的行数为："<< sizeof(arr)/sizeof(arr[0])<<endl;
    cout <<"改数组的列数为："<< sizeof(arr[0])/sizeof(arr[0][0])<<endl;
}



int main()
{
    //Build();
    //GetBiggest();
    //ReverseOrder();
    //Bubble();
    //sunmm();
    
    return 0;
}
*/
