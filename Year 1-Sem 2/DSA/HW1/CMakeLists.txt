cmake_minimum_required(VERSION 3.17)
project(HW1)

set(CMAKE_CXX_STANDARD 14)

add_executable(HW1 App.cpp
        Set.cpp
        Set.h
        SetIterator.cpp
        SetIterator.h
        ShortTest.cpp
        ShortTest.h
        ExtendedTest.cpp
        ExtendedTest.h)