//
// Created by Iulia on 18.03.2021.
//

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

Tutorial_Repo Service_Tutorial::search_by_presenter(string presenter){

    Tutorial_Repo new_repo{};
    if (presenter=="")
    { for (int i=0;i<=get_service_length();i++){

            Tutorial t=get_by_position(i);
            new_repo.add_tutorial(t);

        }

    }
    else
    {
        for (int i=0;i<=get_service_length();i++){
            if(get_by_position(i).get_presenter()==presenter)
            {
                Tutorial t=get_by_position(i);
                new_repo.add_tutorial(t);
            }
        }
    }


    return new_repo;

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

    this->watchlist.add_to_watchlist(tutorial);
}

void Service_Tutorial::delete_from_watchlist(Tutorial tutorial) {

    this->watchlist.remove_from_watchlist(tutorial);
}

