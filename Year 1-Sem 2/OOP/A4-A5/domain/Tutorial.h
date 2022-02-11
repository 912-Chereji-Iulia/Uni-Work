//
// Created by Iulia on 16.03.2021.
//

#pragma once
#include <string>
#include <cstdlib>
using namespace std;

class Tutorial
{
private:
    string title;
    string presenter;
    string duration;
    int nr_likes;
    string link;

public:

    ///constructors
    Tutorial()=default;


    Tutorial(string title, string presenter, string duration,  int nr_likes, string link);

    ~Tutorial(){}

    ///getters
    string get_title();

    string get_presenter();

    string get_duration() ;

    int get_nr_likes()  ;

    string get_link();

    /// function that returns the string reperesentation of a tutorial
    /// \return a string
    string to_string();

    void set_likes(int new_nr);

    void play_in_browser();

    string to_string_without_link();
};