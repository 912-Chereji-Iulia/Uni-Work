//
// Created by Iulia on 10.04.2021.
//

#ifndef A67_912_CHEREJI_IULIA_EXCEPTION_CLASS_H
#define A67_912_CHEREJI_IULIA_EXCEPTION_CLASS_H
#include <string>
using namespace std;

class Exception_Class {

private:
    string message;
public:
    explicit Exception_Class(const string& message);
    ~Exception_Class()= default;
    string get_exception() const ;

};



#endif //A67_912_CHEREJI_IULIA_EXCEPTION_CLASS_H
