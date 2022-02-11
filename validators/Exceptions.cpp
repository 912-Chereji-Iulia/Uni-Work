//
// Created by Iulia on 12.04.2021.
//
#include "Exception_Class.h"


Exception_Class::Exception_Class(const string& message): message(message){}

string Exception_Class::get_exception() const {
    return message;
}
