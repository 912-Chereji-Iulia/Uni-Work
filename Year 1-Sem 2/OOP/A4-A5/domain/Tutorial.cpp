//
// Created by Iulia on 16.03.2021.
//

#include "Tutorial.h"

#include <windows.h>
#include <shellapi.h>

Tutorial::Tutorial(string title, string presenter, string duration,  int nr_likes,
                   string link) {
    this->title=title;
    this->presenter=presenter;
    this->duration=duration;
    this->nr_likes=nr_likes;
    this->link=link;

}

string Tutorial::get_title() {
    return this->title;
}

string Tutorial::get_presenter() {
    return this->presenter;
}

string Tutorial::get_duration()  {
    return this->duration;
}

int Tutorial::get_nr_likes()  {
    return this->nr_likes;
}

void Tutorial::set_likes(int new_nr)
{
    this->nr_likes = new_nr;
}

string Tutorial::get_link() {
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

