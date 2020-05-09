//
//  15_CO_Friend.cpp
//  cpp
//
//  Created by kabun  on 2020/4/30.
//  Copyright © 2020 kabun . All rights reserved.
//

#include <stdio.h>
#include <iostream>
#include <string>
using namespace std;

//============================================友元全局函数==========================================
//class Build
//{
//    //让godgay函数变成友元函数  可以访问build的私有成员
//    friend void GoodGay(Build* building);
//public:
//    Build()
//    {
//        m_BedRoom = "卧室";
//        m_SittingRoom = "客厅";
//
//    }
//public:
//    string m_SittingRoom;
//
//private:
//    string m_BedRoom;
//
//};
////全局函数
//void GoodGay(Build* building)
//{
//    cout << "好基友正在访问：" << building->m_SittingRoom << endl;
//
//    cout << "好基友正在访问：" << building->m_BedRoom << endl;
//
//}
//
//void test01()
//{
//    Build building;
//    GoodGay(&building);
//
//}
//
//int main()
//{
//    test01();
//    return 0;
//}

//============================================友元类==========================================
//class Building;
//class GoodGay
//{
//public:
//    GoodGay();
//    void test();
//    Building* Build;
//
//};
//
//class Building
//{
//    friend class GoodGay;
//public:
//    Building();
//public:
//    string m_SittingRoom;
//
//private:
//    string m_BedRoom;
//};
////类外去写成员函数
//Building :: Building()
//{
//    m_SittingRoom = "客厅";
//    m_BedRoom = "卧室";
//}
//GoodGay::GoodGay()
//{
//    //创建一个建筑物的对象
//    Build = new Building;
//};
//
//void GoodGay::test()
//{
//    cout << "好基友正在访问：：" << Build->m_SittingRoom << endl;
//    cout << "好基友正在访问：：" << Build->m_BedRoom << endl;
//}
//
//void test01()
//{
//    GoodGay gg;
//    gg.test();
//}
//
//int main()
//{
//    test01();
//    return 0;
//}
//============================================友元成员函数==========================================

class Building;
//class GoodGay
//{
//
//public:
//    GoodGay();
//    
//    void visit_1();//让visit  1可以访问Building中的私有成员
//    void visit_2();//让visit  2不可以访问Building中的私有成员
//    
//   
//    Building* build;
//};
//
//class Building
//{
//   friend void GoodGay:: visit_1();//告诉编译器是goodgay下的visit函数
//public:
//    
//    Building();
//    
//    string m_settingroom;
//private:
//    string m_bedroom;
//    
//};
////类外实现成员函数
//Building :: Building()
//{
//    m_settingroom = "和庭";
//    m_bedroom = "睡觉的地方";
//}
//GoodGay :: GoodGay()
//{
//    build = new Building;
//}
//void GoodGay::visit_1()
//{
//    cout << "我要访问：：" << build->m_settingroom << endl;
//    cout << "我要访问：：" << build->m_bedroom << endl;
//}
//void GoodGay::visit_2()
//{
//    cout << "我要访问：：" << build->m_settingroom << endl;
//}
//
//int main()
//{
//    GoodGay gg;
//    gg.visit_1();
//    gg.visit_2();
//    return 0;
//}
