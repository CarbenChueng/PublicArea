//
// Created by Carben Chueng on 2023/10/8.
//
#include <iostream>
#include <string>

using namespace std;

class Person {
public:
    int age;
    char *name;
    float score;
    Person() {
        this->name = "特拉斯";
        cout<<name<<endl;
    }

    void displayInfo() {

        cout << this->age << endl;
    }

    void setNewAgeScore(int age_temp,float score_temp) {
        this->age = age_temp;
        this->score = score_temp;
    }

    ~Person() {
        this->name = "xigouhanshu";
        cout<<name<<endl;
    }

};


int main() {
    Person laowang;
    Person laozhang;//栈空间，执行完自动释放空间
//    Person *p = new Person();//new是堆空间，需要用delete手动释放空间
    laowang.age = 18;
    laozhang.age = 19;

    laowang.displayInfo();
    laozhang.displayInfo();
    return 0;
}