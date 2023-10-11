cmake_minimum_required(VERSION 3.19)
project(Code)

set(CMAKE_CXX_STANDARD 14)

include_directories(.)
include_directories(_C++Learn)
include_directories(_C++Project)

add_executable(Code
        _C++Learn/00_test.cpp _C++_DG/_01_.cpp)
        #_C++Project/P01_AddressBookSystem.cpp)
