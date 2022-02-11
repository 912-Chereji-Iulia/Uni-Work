//
// Created by Iulia on 25.03.2021.
//

#pragma once

#include "../domain/Dyn-Array.h"
class Watchlist {

private:
    Dyn_Array<Tutorial> tutorials;
    int current_tutorial;
public:
    Watchlist();

    void add_to_watchlist( const Tutorial& tutorial);
    void remove_from_watchlist(Tutorial tutorial);
    Tutorial get(int i);
    int size_of_watchlist();
    int find_pos_by_link(string link);
};



