//
// Created by Iulia on 18.03.2021.
//

#pragma once

#include "../repo/Watchlist.h"
#include "../repo/Repo.h"

class Service_Tutorial
{
private:
    Tutorial_Repo repo;
    Watchlist watchlist;

public:
    ///constructor and destructor
    Service_Tutorial(){}

    ~Service_Tutorial(){}


    /// function that adds a new tutorial
    /// \param title of the new tutorial
    /// \param presenter of the new tutorial
    /// \param duration of the new tutorial
    /// \param likes of the new tutorial
    /// \param link of the new tutorial
    /// \return 1 if it was added or -1 otherwise
    int add_service(string title,string presenter,string duration,int likes,string link);

    /// function that deletes a tutorial
    /// \param title of the tutorial to be deleted
    /// \return 1 if it was deleted or -1 otherwise
    int delete_service(string title);

    /// function that updates a tutorial
    /// \param title of the tutorial to be updated
    /// \param t the new tutorial
    /// \return 1 if it was updated or -1 otherwise
    int update_service(string title, Tutorial t);

    Tutorial_Repo search_by_presenter(string presenter);

    /// get the length of the service
    /// \return
    int get_service_length();

    /// function to return a tutorial on a given position
    /// \param position- the position of the wanted tutorial
    /// \return the tutorial on that position
    Tutorial get_by_position(int position);

    void add_to_watchlist(Tutorial tutorial);

    void delete_from_watchlist(Tutorial tutorial);

    Watchlist get_watchlist() const {return watchlist;}

    Tutorial_Repo get_repo() const {return repo;}
};
