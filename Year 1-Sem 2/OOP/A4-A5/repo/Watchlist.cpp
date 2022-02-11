//
// Created by Iulia on 25.03.2021.
//

#include "Watchlist.h"

Watchlist::Watchlist() {
    this->current_tutorial=0;
}

void Watchlist::add_to_watchlist( const Tutorial &tutorial) {
    this->tutorials.add(tutorial);

}

int Watchlist::size_of_watchlist() {
    return this->tutorials.get_length();
}

void Watchlist::remove_from_watchlist(Tutorial tutorial) {
    for(int i=0; i<this->tutorials.get_length();i++)
        if(this->tutorials.get_all()[i].get_title()==tutorial.get_title())
        {
            this->tutorials.remove(i);
            break;
        }

}
int Watchlist::find_pos_by_link(string link)
{
    for (int i=0;i<this->size_of_watchlist();i++)
        if (this->get(i).get_link()==link)
            return i;
    return -1;

}

Tutorial Watchlist::get(int i){
    if (i>=0 && i<this->size_of_watchlist())
        return this->tutorials.get_all()[i];
    return Tutorial{};
}