cmake_minimum_required(VERSION 3.17)
project(HW3)

set(CMAKE_CXX_STANDARD 14)

include_directories(.)

add_executable(HW3
        App.cpp
        ExtendedTest.cpp
        ExtendedTest.h
        ShortTest.cpp
        ShortTest.h
        SortedBag.cpp
        SortedBag.h
        SortedBagIterator.cpp
        SortedBagIterator.h)
