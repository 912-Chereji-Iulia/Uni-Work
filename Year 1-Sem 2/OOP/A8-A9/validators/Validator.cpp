//
// Created by Iulia on 10.04.2021.
//

#include <algorithm>
#include "Validator.h"

void Validator::valid_link(const string& link) {

    if(link.length()<0)
        throw (Exception_Class("Invalid link!"));

}

void Validator::valid_int(const string& integer) {

    if (!std::all_of(integer.begin(),integer.end(),::isdigit))
        throw (Exception_Class("Invalid integer"));
    int nr=stoi(integer);
    if (nr<0)
        throw (Exception_Class("Invalid integer"));
}

void Validator::valid_duration(string duration) {
    if (duration.length()!=5)
        throw (Exception_Class("Invalid duration"));
    if (duration[2]!=':')
        throw (Exception_Class("Invalid duration"));
    else
    {
        if(int(duration[0])-48<0 || int(duration[0])-48>=6)
            throw (Exception_Class("Invalid duration"));
        if(int(duration[1])-48<0 || int(duration[1])-48>=10)
            throw (Exception_Class("Invalid duration"));
        if(int(duration[3])-48<0 || int(duration[3])-48>=6)
            throw (Exception_Class("Invalid duration"));
        if(int(duration[4])-48<0 || int(duration[4])-48>=10)
            throw (Exception_Class("Invalid duration"));

    }

}

void Validator::valid_presenter(const string& presenter) {
    if(presenter.length()<0)
        throw (Exception_Class("Invalid presenter!"));

}

void Validator::valid_title(const string& title) {

    if(title.length()<0)
        throw (Exception_Class("Invalid title!"));

}
