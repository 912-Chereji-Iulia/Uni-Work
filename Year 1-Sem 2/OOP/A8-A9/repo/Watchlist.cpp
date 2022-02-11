//
// Created by Iulia on 25.03.2021.
//

#include <fstream>
#include <algorithm>
#include "Watchlist.h"
#include "Repo.h"


void Watchlist::add_to_watchlist( const Tutorial &tutorial) {
    this->tutorials->push_back(tutorial);
    this->save();

}

int Watchlist::size_of_watchlist() {
    return this->tutorials->size();
}

void Watchlist::remove_from_watchlist(Tutorial tutorial) {
    auto it=find_if(this->tutorials->begin(), this->tutorials->end(), [tutorial](const Tutorial& t){
        return t.get_title()==tutorial.get_title();
    });
    if(it!=this->tutorials->end())
        this->tutorials->erase(it);
    else
        throw(Exception_Class("The tutorial doesn't exist"));
    this->save();


}
int Watchlist::find_by_link(string link)
{
    auto it=find_if(this->tutorials->begin(), this->tutorials->end(), [&link](const Tutorial& t){
        return t.get_link()==link;
    });
    if(it!=this->tutorials->end())
        throw (Exception_Class("Tutorial with this link already in the watchlist"));

    return 1;
}

Tutorial Watchlist::get(int i){
    if (i>=0 && i<this->size_of_watchlist())
        return this->tutorials->at(i);
    return Tutorial{};
}

Watchlist::Watchlist() {
    tutorials=new vector<Tutorial>();

}

Watchlist::~Watchlist(){
    delete tutorials;
}


void Watchlist::save() {

    ofstream out(file_name);
    vector<Tutorial>* tutorials=this->get_all();
    for (auto &i: *tutorials){
        out<<i;
    }
    out.close();
}

Watchlist::Watchlist(const string &file_name) {

    this->file_name=file_name;
}

void Watchlist::load() {
    ifstream f(this->file_name);
    if(!f.is_open())
        return;
    Tutorial t{};
    while(f>>t)
        this->add_to_watchlist(t);
    f.close();

}

