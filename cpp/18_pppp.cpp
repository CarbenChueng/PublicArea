//
// Created by Administrator on 2020/5/15 0015.
//
#include <iostream>
#include <string>

//��̬��̬����������
//1���м̳й�ϵ
//2������Ҫ��д������麯��

//��̬��̬��ʹ�ã������ָ���������ִ���������
using namespace std;

class Animal{
public:
    //�麯��
    virtual void speak()
    {
        cout << "������˵��" << endl;
    }

};

class Cat: public Animal
{
public:
    void speak()
    {
        cout << "ëëëëë��˵��" << endl;
    }
};

class Dog : public Animal
{
public:
    void speak()
    {
        cout << "С��С��С��С����˵��" << endl;
    }
};
//��ַ��󶨣��ڱ���׶ξ�ȷ���˺����ĵ�ַ
//�����ִ��è˵�����ĳ����н׶ΰ󶨣���󶨣�
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
