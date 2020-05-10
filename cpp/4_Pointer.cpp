//
//  4_Pointer.cpp
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


/*
//指针访问数组
void Visit()
{
    int arr[] = {1,2,3,4,5,6};
    int* p = arr;
    
    for(int i = 0;i< 6;i++)
    {
        cout << *p <<endl;
        p++;
    }
}

//地址传递
void swap(int* h,int* k)
{
    int temp = *h;
    *h = *k;
    *k = temp;
    
}

//数组传进函数
void BubbleSort(int* arr,int len)
{
    for(int i = 0; i < len;i++)
    {
        for(int l =0; l<len-i-1;l++)
        {
            if(arr[l]>arr[l+1])
            {
                int temp = arr[l];
                arr[l] = arr[l+1];
                arr[l+1] = temp;
            }
            
        }
        
    }
}

void PrintArr(int* h,int len)
{
    for(int i = 0; i<len; i++)
    {
        cout << h[i] <<"  ";
    }
}

int main()
{
    int a = 10;
    int b = 20;
    
    swap(&a, &b);
    
    cout << a <<endl;
    cout << b <<endl;
    
    int arr[6] = {1,22,15,33,57,32};
    int len = sizeof(arr)/sizeof(arr[0]);
    BubbleSort(arr,len);
    PrintArr(arr,len);
    //Visit();
    
    return 0;
}

 */

//class Person
//{
//public:
//    void ShowClassName()
//    {
//        cout << "哈哈" << endl;
//    }
//    void ShowPersonAge()
//    {
//        //报错，因为是空指针
//        cout << age << endl;
//    }
//    int age;
//};
//
//void test01()
//{
//    Person* p = NULL;
//    p->ShowClassName();
//    p->ShowPersonAge();
//}
//int main()
//{
//    test01();
//    return 0;
//}
