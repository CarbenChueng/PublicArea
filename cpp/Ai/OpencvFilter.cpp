//
// Created by kabun on 2020-06-16.
//
#include <opencv2/opencv.hpp>
using namespace std;

//int main()
//{
//    cv::Mat img = cv::imread("../Image/1.jpg");
//    cv::Mat img2 = cv::imread("../Image/2.jpg");
//    cv::Mat ds;
    //自定义滤波器(高通)
//    cv::Mat m = (cv::Mat_<double >(3,3)<<1,1,0,1,0,-1,0,-1,-1);
//    cv::filter2D(img,ds,-1,m);
    //低通
//    cv::blur(img,ds,cv::Size(3,3));//均值滤波
//    cv::GaussianBlur(img,ds,cv::Size(3,3),1,1);//高斯滤波
//    cv::medianBlur(img,ds,3);//中值滤波
//    cv::bilateralFilter(img,ds,9,75,75);//双边滤波
//    高通滤波
//    cv::Laplacian(img,ds,-1,1);//拉普拉斯滤波器
//    求梯度
//    cv::Sobel(img2,ds,-1,1,0);
//    cv::Sobel(img2,ds,-1,0,1);
//    cv::Scharr(img2,ds,-1,1,0);
//
//    cv::imshow("j",img2);
//    cv::imshow("k",ds);
//
//    cv::waitKey(0);
//    return  0;
//
//};

int main()
{
    cv::Mat img,img_gary,bin_img;
    img = cv::imread("../Image/14.jpg");

    cv::cvtColor(img,img_gary,cv::COLOR_BGR2GRAY);
    cv::threshold(img_gary,bin_img,127,255,cv::THRESH_BINARY|cv::THRESH_OTSU);

    vector<vector<cv::Point>> contours;
    vector<cv::Vec4i> vec_4f;
    cv::findContours(bin_img,contours,vec_4f,cv::RETR_TREE,cv::CHAIN_APPROX_SIMPLE);

    cv::drawContours(img,contours,-1,cv::Scalar(255,0,0),3);

    cv::imshow("sd",img);
    cv::waitKey(0);


    return 0;
}