//
// Created by kabun on 2020-06-30.
//
#include <iostream>
using namespace std;

class Animal
{
public:
    //虚函数
    virtual void sepak()
    {
        cout << "动物在说话" << endl;
    }

};

class Cat : public Animal
{
public:
    void speak()
    {
        cout << "小猫在说话" << endl;
    }
};

void doSpeak(Animal& animal)
{
    animal.sepak();
}

void test()
{
    Cat cat;
    doSpeak(cat);
}


int main()
{
    test();

    return 0;
}

