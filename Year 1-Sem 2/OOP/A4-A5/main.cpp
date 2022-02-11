//
// Created by Iulia on 18.03.2021.
//
#include <iostream>
#include "repo/Repo.h"
#include "service/Service.h"
#include "ui/UI.h"
#include "tests/Tests.h"
int main()
{
    Tests tests;
    tests.test_all();


    UI ui{};
    ui.start_me();
    return 0;
}