cmake_minimum_required(VERSION 3.17)
project(a23_912_Chereji_Iulia C)

set(CMAKE_C_STANDARD 11)



add_executable(a23_912_Chereji_Iulia
        Country.c
        Country.h
        Array.c
        Array.h
        UI.c
        UI.h
        Country-Repo.c
        Country-Repo.h
        Service.c
        Service.h
        main.c
        tests.c
        tests.h
        Operations-List.c
        Operations-List.h)
