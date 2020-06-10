cmake_minimum_required(VERSION 3.14)
project(CppProject)

set(CMAKE_CXX_STANDARD 14)

set(OpenCV_DIR D:/CppLib/opencv/build/x64/vc15/lib)#OpenCV的编译路径

find_package(OpenCV REQUIRED)#找到OpenCV的相应的库函数

add_executable(CppProject Ai/OpencvStudy.cpp)#要编译的源码
target_link_libraries(CppProject ${OpenCV_LIBS})#编译时需要的OpenCV的库连接到当前的项目中
#将动态链接库拷贝到当前的程序所在的文件夹
if (MSVC)
    file(GLOB OPENCV_DLLS "D:/CppLib/opencv/build/x64/vc15/bin/*.dll")
    add_custom_command(TARGET CppProject
            POST_BUILD
            COMMAND ${CMAKE_COMMAND} -E copy_if_different
            ${OPENCV_DLLS}
            $<TARGET_FILE_DIR:CppProject>)
endif (MSVC)


