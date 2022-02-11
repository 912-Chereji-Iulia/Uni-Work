//
// Created by Iulia on 18.03.2021.
//

#include "Repo.h"
#include <string.h>
#include <fstream>
#include <iostream>
#include <vector>

using namespace std;


int Tutorial_Repo::get_repo_length() {
    return this->tutorials.get_length();

}

int Tutorial_Repo::add_tutorial(Tutorial& tutorial) {

    int pos=find_pos_by_link(tutorial.get_link());
    if(pos!=-1)
        return -1;
    this->tutorials.add(tutorial);
    return 1;
}

int Tutorial_Repo::find_pos_by_title(string title)
{
    for (int i=0;i<this->get_repo_length();i++)
        if (this->get_by_pos_repo(i).get_title()==title)
            return i;
    return -1;

}

int Tutorial_Repo::find_pos_by_link(string link)
{
    for (int i=0;i<this->get_repo_length();i++)
        if (this->get_by_pos_repo(i).get_link()==link)
            return i;
    return -1;

}

int Tutorial_Repo::update_tutorial(string title, Tutorial new_tutorial){

    int pos=this->find_pos_by_title(title);
    if(pos==-1)
        return -1;
    this->tutorials.update(new_tutorial,pos);
    return 1;

}


int Tutorial_Repo::delete_tutorial(string title) {
    int position=find_pos_by_title(title);
    if(position==-1)
        return -1;
    this->tutorials.remove(position);
    return 1;
}

Tutorial Tutorial_Repo::get_by_pos_repo(int position)
{
    return this->tutorials.get_by_pos_dyn_arr(position);
}
