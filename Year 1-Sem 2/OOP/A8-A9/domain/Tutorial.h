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
    string get_title()const;

    string get_presenter()const;

    string get_duration() const;

    int get_nr_likes()  const;

    string get_link()const;

    /// function that returns the string reperesentation of a tutorial
    /// \return a string
    string to_string();

    void set_likes(int new_nr);

    void play_in_browser();

    string to_string_without_link();

    bool operator==(const Tutorial&t);

    friend istream &operator>>(istream &in, Tutorial &tutorial);
    friend ostream &operator<<(ostream &os, const Tutorial &tutorial);
};