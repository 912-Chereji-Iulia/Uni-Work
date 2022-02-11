//
// Created by Iulia on 16.03.2021.
//

#include "Tutorial.h"

#include <windows.h>
#include <shellapi.h>
using namespace std;
#include <iostream>
#include <sstream>
#include <vector>


Tutorial::Tutorial(string title, string presenter, string duration,  int nr_likes,
                   string link) {
    this->title=title;
    this->presenter=presenter;
    this->duration=duration;
    this->nr_likes=nr_likes;
    this->link=link;

}

string Tutorial::get_title() const{
    return this->title;
}

string Tutorial::get_presenter() const{
    return this->presenter;
}

string Tutorial::get_duration() const  {
    return this->duration;
}

int Tutorial::get_nr_likes() const {
    return this->nr_likes;
}

void Tutorial::set_likes(int new_nr)
{
    this->nr_likes = new_nr;
}


string Tutorial::get_link() const{
    return this->link;
}

void Tutorial::play_in_browser(){
    string play=this->link;
    ShellExecuteA(NULL, "open", play.c_str(), NULL, NULL, SW_SHOWNORMAL);
}


string Tutorial::to_string_without_link() {
    string result("Title: "+this->title+"| Presenter: "+ this->presenter+"| Duration: "+ this->duration+"| Likes: "+ ::to_string(this->nr_likes)+"\n");
    return result;
}


string Tutorial::to_string() {
    string result("Title: "+this->title+"| Presenter: "+ this->presenter+"| Link: "+this->link+"| Duration: "+ this->duration+"| Likes: "+ ::to_string(this->nr_likes)+"\n");
    return result;
}

vector<string> tokenize(string str, char del){
    vector<string> result;
    stringstream ss(str);
    string token;
    while (getline(ss, token, del))
        result.push_back(token);

    return result;
}

bool Tutorial::operator==(const Tutorial &t) {
    return t.get_title()==this->get_title() && t.get_presenter()==this->get_presenter() &&
            t.get_nr_likes()==this->get_nr_likes() && t.get_duration()==this->get_duration() &&t.get_link()==this->get_link() ;
}

istream &operator>>(istream &in, Tutorial &tutorial) {
    string line;
    getline(in,line);
    vector <string> tokens=tokenize(line,',');
    if(tokens.size()!=5)
        return in;
    tutorial.title=tokens[0];
    tutorial.presenter=tokens[1];
    tutorial.duration=tokens[2];
    tutorial.nr_likes=stoi(tokens[3]);
    tutorial.link=tokens[4];

    return in;
}

ostream &operator<<(ostream &os, const Tutorial &tutorial) {
    os<<tutorial.title<<","<<tutorial.presenter<<","<<tutorial.duration<<","<<tutorial.nr_likes<<","<<tutorial.link<<endl;
    return os;
}

