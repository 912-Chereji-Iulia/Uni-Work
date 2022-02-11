//
// Created by Iulia on 16.04.2021.
//

#include <fstream>
#include "CSV.h"
#include "../validators/Exception_Class.h"



void CSV::save() {

    ofstream out(file_name);
    vector<Tutorial>* tutorials=this->get_all();
    for (auto &t: *tutorials){
        out<<t;
    }
    out.close();
}


void CSV::open() {

    system("notepad.exe C:\\Users\\Iulia\\Desktop\\Info\\a67-912-Chereji-Iulia\\cmake-build-debug\\Testing\\watchlist.csv");

}

CSV::~CSV() = default;

CSV::CSV(const string &file_name) :File_Repo(file_name) {
    this->file_name=file_name;
}

