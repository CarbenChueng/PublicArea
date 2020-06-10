//
// Created by Administrator on 2020/6/9 0009.
//
#include <opencv2/opencv.hpp>
#include <vector>
#include <iostream>
using namespace std;

int main(){
//=====================================看图===========================================
//    cv::Mat img = cv::imread("D://CppProject/Image/mao.jpg");
//    cout << img.rows << img.cols << endl;
//    cv::imshow("asd",img);
//    cv::waitKey(0);
//    cout << "asdasd" << endl;


//=====================================画图===========================================
//    cv:: Mat img = cv::Mat(200,300,CV_8UC3,cv::Scalar(255,0,0));
//方法一：不建议
//    for (int i = 0; i <img.rows;i++)
//    {
//        for (int l = 0; l <img.rows;l++)
//        {
//            img.at<cv::Vec3b>(i,l)[0] = 0;
//            img.at<cv::Vec3b>(i,l)[1] = 255;
//            img.at<cv::Vec3b>(i,l)[2] = 255;
//        }
//    }

//方法二
//    vector<cv::Mat> ms;
//    cv::split(img,ms);//通道切割
//    ms[0] = cv::Scalar(0); //蓝是0
//    ms[1] = cv::Scalar(255);
//    ms[2] = cv::Scalar(255);
//    cv::merge(ms,img);//通道合并
//    cv:: imwrite("write_pic.jpg",img);


//=====================================视频，摄像头===========================================
//    cv::VideoCapture cap;
//    cap = cv::VideoCapture("http://ivi.bupt.edu.cn/hls/cctv1hd.m3u8");
//    while (true)
//    {
//        cv::Mat frame;
//        cap>>frame;
//        cv::imshow("frame",frame);
//        cv::waitKey(41);
//    }
//    cap.release();
//    cv::destroyAllWindows();


    return 0;
}