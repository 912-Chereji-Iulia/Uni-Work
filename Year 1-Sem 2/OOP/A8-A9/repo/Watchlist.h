//
// Created by Iulia on 25.03.2021.
//

#pragma once

#include "../domain/Dyn-Array.h"
#include <vector>
class Watchlist {

protected:
    vector<Tutorial>* tutorials;
    virtual void save();
    string file_name;

public:
    Watchlist();
    Watchlist(const string &file_name);
    ~Watchlist();

    void add_to_watchlist( const Tutorial& tutorial);
    void remove_from_watchlist(Tutorial tutorial);
    Tutorial get(int i);
    int size_of_watchlist();
    int find_by_link(string link);
    vector<Tutorial>* get_all(){return tutorials;}
    void load();

};


