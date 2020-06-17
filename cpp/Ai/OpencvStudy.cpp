//
// Created by Administrator on 2020/6/9 0009.
//
#include <opencv2/opencv.hpp>
#include <vector>
#include <iostream>

using namespace std;

int main() {
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
//
//
//    while (true)
//    {
//        cv::Mat frame;
//        cap>>frame;
//        cv::imshow("frame",frame);
//        cv::waitKey(41);
//
////        if (cv::waitKey(41) & 0XFF == "q")
////        {
////            break;
////        }
//    }
//    cap.release();
//    cv::destroyAllWindows();
//
//




//=====================================抠图===========================================
//    cv::Mat img = cv::imread("../Image/11.jpg");
//    cv::Mat hsv;
//    cv::Mat mask;
//    cv:: cvtColor(img,hsv,cv::COLOR_BGR2HSV);
//    cv::inRange(hsv,cv::Scalar(1,110,100),cv::Scalar(200,255,200),mask);
//    cv::imshow("pic",img);
//    cv::imshow("mas",mask);
//    cv::waitKey(0);
//    cv::destroyAllWindows();



//=====================================图上划线===========================================
//    cv::Mat img = cv::imread("../Image/food.jpg");
//    线
//    cv::line(img,cv::Point(100,30),cv::Point(210,180),cv::Scalar(0,0,255),2);
//    矩形
//    cv::rectangle(img,cv::Point(100,30),cv::Point(210,180),cv::Scalar(0,0,255),2);
//    圆
//    cv::circle(img,cv::Point(100,60),60,cv::Scalar(0,0,255),2);
//    椭圆
//    cv::ellipse(img,cv::Point(200,160),cv::Point(150,90),0,0,360,cv::Scalar(255,0,0),2);
//    多边形
//    std::vector<cv::Point> contour;
//    contour.push_back(cv::Point(10,5));
//    contour.push_back(cv::Point(120,115));
//    contour.push_back(cv::Point(150,25));
//    contour.push_back(cv::Point(90,95));
//    contour.push_back(cv::Point(200,250));
//    contour.push_back(cv::Point(300,35));
//
//    cv::polylines(img,contour, true,cv::Scalar(0,255,0),2);
//    图片，点的集合，是否闭合，颜色，粗细
//    cv::imshow("pic",img);
//
//    cv::waitKey(0);
//    cv::destroyAllWindows();



//=====================================图上写字===========================================

//    cv::Mat img = cv::imread("../Image/cute.jpg");
//    cv::putText(img,"HELLO BABY",cv::Point(100,150),cv::FONT_HERSHEY_SIMPLEX
//            ,1,cv::Scalar(255,0,0),3,cv::LINE_AA);
//    cv::imshow("pic",img);
//
//    cv::waitKey(0);
//    cv::destroyAllWindows();




//=====================================阀值===========================================
//    全局二值化
//    cv::Mat img = cv::imread("../Image/cute.jpg");
//    cv::Mat gry;
//
//    cv::cvtColor(img, gry, cv::COLOR_BGR2GRAY);
//    cv::Mat binnn;
//
//    cv::threshold(gry, binnn, 0, 255, cv::THRESH_BINARY | cv::THRESH_OTSU);
//    cv::imshow("pic", img);
//    cv::imshow("pisc", binnn);
//
//    cv::waitKey(0);
//    cv::destroyAllWindows();



//    cv::Mat img = cv::imread("../Image/paint.jpg");
//
//    cv::imshow("pisc", img);
//
//    cv::waitKey(0);
//    cv::destroyAllWindows();



//    局部二值化
//    cv::Mat img = cv::imread("../Image/2.jpg",0);
//    cv::Mat ds1,ds2,ds3;
//
//    cv::threshold(img,ds1,127,255,cv::THRESH_BINARY);
//    cv::adaptiveThreshold(img,ds2,255,cv::ADAPTIVE_THRESH_MEAN_C,
//            cv::THRESH_BINARY,11,2);
//    cv::adaptiveThreshold(img,ds3,255,cv::ADAPTIVE_THRESH_GAUSSIAN_C,
//            cv::THRESH_BINARY,11,2);
//
//    cv::imshow("ds1",ds1);
//    cv::imshow("ds2",ds2);
//    cv::imshow("ds3",ds3);
//
//    cv::waitKey(0);
//    cv::destroyAllWindows();

//=====================================图片加减（混合）===========================================
//    cv::Mat x = (cv::Mat_<uchar>(2,1)<<250,34);//uchar无符号单字节
//    cv::Mat y = (cv::Mat_<uchar>(2,1)<<10,100);
//
//    cv::Mat addrest,subrst;
//    cv::add(x,y,addrest);
//    cv::subtract(x,y,subrst);
//
//    std::cout<< addrest <<endl;
//    std::cout<< subrst <<endl;




//=====================================图片变换===========================================
//    cv::Mat pit = cv::imread("../Image/food.jpg");
//
//    cv::Mat zhuan;
//    尺寸
//    cv::resize(pit,zhuan,cv::Size(300,300));
//    翻转
//    cv::flip(pit,zhuan,2);
//    仿射变换
//    cv:: Mat m = (cv::Mat_<double>(2,3)<<
//            1,0,50,0,1,50);
//    cv::Mat m = cv::getRotationMatrix2D(cv::Point(pit.rows/2,
//            pit.cols/2),45,0.7);

//    cv::warpAffine(pit,zhuan,m,pit.size());


//透明变换：放大镜
//    cv::Point2f pts1[] = {cv::Point2f(25,30),cv::Point2f(179,25),
//                          cv::Point2f(12,188),cv::Point2f(189,190)};
//
//    cv::Point2f pts2[] = {cv::Point2f(0,0),cv::Point2f(500,0),
//                          cv::Point2f(0,500),cv::Point2f(500,500)};
//    cv::Mat m = cv::getPerspectiveTransform(pts1,pts2);
//    cv::warpPerspective(pit,zhuan,m,pit.size());
//
//    cv::imshow("a",pit);
//    cv::imshow("b",zhuan);
//    cv::waitKey(0);


    cv::Mat img1,img2,ds,kernel;
    kernel = cv::getStructuringElement(cv::MORPH_RECT,cv::Size(3,3));
    img1 = cv::imread("../Image/3.jpg");
    img2 = cv::imread("../Image/4.jpg");

    cv::dilate(img1,ds,kernel);//膨胀
//    cv::erode(img1,ds,kernel);//腐蚀
//    cv::morphologyEx(img2,ds,cv::MORPH_OPEN,kernel);//开
//    cv::morphologyEx(img2,ds,cv::MORPH_CLOSE,kernel);//闭
//    cv::morphologyEx(img1,ds,cv::HOUGH_GRADIENT,kernel);//梯度
//    cv::morphologyEx(img2,ds,cv::MORPH_TOPHAT,kernel);//顶帽
//    cv::morphologyEx(img2,ds,cv::MORPH_BLACKHAT,kernel);//黑帽
    cv::imshow("s",img1);
    cv::imshow("a",ds);
    cv::waitKey(0);
    return 0;
}
