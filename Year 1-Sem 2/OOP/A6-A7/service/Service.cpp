//
// Created by Iulia on 18.03.2021.
//

#include <algorithm>
#include "Service.h"


int Service_Tutorial::add_service(string title, string presenter, string duration, int likes,
                                  string link) {
    Tutorial tutorial{title,presenter,duration,likes, link};
    return this->repo.add_tutorial(tutorial);

}

int Service_Tutorial::delete_service(string title) {

    return this->repo.delete_tutorial(title);

}
int Service_Tutorial::update_service(string title, Tutorial t) {
    return this->repo.update_tutorial(title, t);
}

vector<Tutorial> Service_Tutorial::search_by_presenter(string presenter){

    return this->repo.search_by_presenter(presenter);

}

int Service_Tutorial::get_service_length()
{
    return this->repo.get_repo_length();
}

Tutorial Service_Tutorial::get_by_position(int position)
{
    return this->repo.get_by_pos_repo(position);
}

void Service_Tutorial::add_to_watchlist(Tutorial tutorial) {

    this->watchlist->add_to_watchlist(tutorial);
}

void Service_Tutorial::delete_from_watchlist(Tutorial tutorial) {

    this->watchlist->remove_from_watchlist(tutorial);
}


void Service_Tutorial::load_repo(){
    this->repo.load();
}


Service_Tutorial::Service_Tutorial(const Tutorial_Repo &repo,  File_Repo* watchlist) {
    this->repo=repo;
    this->watchlist =  watchlist;
}



void Service_Tutorial::open_app() {

    this->watchlist->open();
}


