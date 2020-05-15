//
// Created by Administrator on 2020/5/15 0015.
//
#include <iostream>
#include <string>

//动态多态满足条件：
//1：有继承关系
//2：子类要重写父类的虚函数

//动态多态是使用：父类的指针或者引用执行子类对象
using namespace std;

class Animal{
public:
    //虚函数
    virtual void speak()
    {
        cout << "动物在说话" << endl;
    }

};

class Cat: public Animal
{
public:
    void speak()
    {
        cout << "毛毛毛毛毛在说话" << endl;
    }
};

class Dog : public Animal
{
public:
    void speak()
    {
        cout << "小狗小狗小狗小狗在说话" << endl;
    }
};
//地址早绑定，在编译阶段就确定了函数的地址
//如果想执行猫说话，改成运行阶段绑定（晚绑定）
void dospeak(Animal& sha)
{
    sha.speak();

}
void test()
{
    Cat cat;
    dospeak(cat);

    Dog dog;
    dospeak(dog);
}

int main()
{

    test();
    return 0;
}
