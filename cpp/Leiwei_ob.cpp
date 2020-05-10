//
//  Leiwei_ob.cpp
//  cpp
//
//  Created by kabun  on 2020/4/22.
//  Copyright © 2020 kabun . All rights reserved.
//

#include <stdio.h>
#include <iostream>
#include <string>
#include <ctime>
using namespace std;

/*
struct Person
{
    string name;
    int age;
    
    Person()
    {
        this->name = "李小龙";
        this->age = 26;
    }
    Person(string name,int age)
    {
        this->name = name;
        this->age = age;
    }
    
    void func()
    {
        cout << this->name <<",\t" << this->age << endl;
    }
    
    ~Person()
    {
        cout << "搞掂就完事了" << endl;
    }
    
};

void clazz_show()
{
    
    Person p;
    p.func();
    
    Person* JJ = new Person("静静",23);
    JJ->func();
    (*JJ).func();
    
}

int main()
{
    clazz_show();
}
*/

//================================================函数继承===================================================
/*
class Animal
{
protected:
    string sex;
    
public:
    
    Animal(string o_sex):sex(o_sex){}
    
    void fly()
    {
        cout << "我tm要飞翔，飞得更高" << endl;
    }
};
class Cat:public Animal
{
public:
    Cat(string o_sex):Animal(o_sex){}
    //定义一个虚方法
    virtual void fly()
    {
        cout << "飞飞飞飞i俄方i俄方i额"  << this->sex <<":"<<endl;
    }
    
};

void inherit_show()
{
    Animal* MyCat = new Cat("公");
    MyCat->fly();
    delete MyCat;
}

int main()
{
    inherit_show();
    
    
    
    return 0;
}
*/

//================================================函数模版===================================================
/*
template <typename T>
T add(T& a,T& b)
{
    return a+b;
}

int main()
{
    int x = 3,y =10;//还是必须要类型相同
    //float y = 1.3;
    string n1 = "李小龙", n2 = "好劲啊";
    cout << add(x, y)<< endl;
    cout << add(n1, n2)<< endl;
    return 0;
}
*/

//================================================类模版===================================================
/*
int main()
{
    int x = 3;
    float y = 1.3;
    //string n1 = "李小龙", n2 = "好劲啊";
    cout << x+ y<< endl;
    //cout << add(n1, n2)<< endl;
    return 0;
}

*/
