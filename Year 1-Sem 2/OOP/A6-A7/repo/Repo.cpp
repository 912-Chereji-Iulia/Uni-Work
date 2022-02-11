//
// Created by Iulia on 18.03.2021.
//

#include "Repo.h"
#include <string.h>
#include <fstream>
#include <iostream>
#include <vector>
#include <algorithm>
#include "../validators/Exception_Class.h"


using namespace std;

vector<Tutorial> Tutorial_Repo::search_by_presenter(string presenter){

    vector<Tutorial> new_repo;

    auto iterator=copy_if(this->tutorials.begin(), this->tutorials.end(), back_inserter(new_repo),[&presenter](Tutorial t){
        if(!presenter.empty())
            return t.get_presenter()==presenter;
        else
            return true;
    });

    return new_repo;

}

int Tutorial_Repo::get_repo_length() {
    return this->tutorials.size();
}

int Tutorial_Repo::add_tutorial(Tutorial& tutorial) {

    auto iterator=find_if(this->tutorials.begin(), this->tutorials.end(), [&tutorial](const Tutorial& t){return t.get_link()==tutorial.get_link();});
    if(iterator!=this->tutorials.end())
        throw (Exception_Class("Tutorial with this link already in the repo"));
    this->tutorials.push_back(tutorial);
    save();
    return 1;
}



int Tutorial_Repo::update_tutorial(string title, Tutorial new_tutorial){

    auto iterator=find_if(this->tutorials.begin(), this->tutorials.end(), [&title](const Tutorial& t){return t.get_title()==title; });

    if(iterator!=this->tutorials.end())
        *iterator=new_tutorial;
    else
        throw(Exception_Class("The tutorial doesn't exist"));
    save();
    return 1;

}


int Tutorial_Repo::delete_tutorial(string title) {
    auto iterator=find_if(this->tutorials.begin(), this->tutorials.end(), [&title](const Tutorial& t) {return t.get_title()==title;});

    if(iterator!=this->tutorials.end())
        this->tutorials.erase(iterator);
    else
        throw(Exception_Class("The tutorial doesn't exist"));
    save();
    return 1;
}

Tutorial Tutorial_Repo::get_by_pos_repo(int position)
{
    return this->tutorials[position];
}

void Tutorial_Repo::save(){
    ofstream f(this->file_name);
    if(!f.is_open())
        return;
    for(auto t: this->tutorials)
        f<<t;
    f.close();

}

void Tutorial_Repo::load(){
    ifstream f(this->file_name);
    if(!f.is_open())
        return;
    Tutorial t{};
    while(f>>t)
        this->add_tutorial(t);
    f.close();
}



Tutorial_Repo::Tutorial_Repo(const string &file_name) {
    this->file_name=file_name;

}

std::ostream &operator<<(std::ostream &out, const Exception_Class &ex){
    out<< ex.get_exception();
    return out;
}