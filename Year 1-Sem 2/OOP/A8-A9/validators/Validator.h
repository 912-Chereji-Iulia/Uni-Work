//
// Created by Iulia on 10.04.2021.
//

#ifndef A67_912_CHEREJI_IULIA_VALIDATOR_H
#define A67_912_CHEREJI_IULIA_VALIDATOR_H

#include <string>
#include "Exception_Class.h"
using namespace std;
class Validator {
public:
    static void valid_title(const string& title);
    static void valid_presenter(const string& presenter);
    static void valid_duration(string duration);
    static void valid_int(const string& integer);
    static void valid_link(const string& link);
};


#endif //A67_912_CHEREJI_IULIA_VALIDATOR_H
