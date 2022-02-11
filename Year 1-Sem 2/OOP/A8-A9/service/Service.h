//
// Created by Iulia on 18.03.2021.
//

#pragma once


#include "../repo/Watchlist.h"
#include "../repo/Repo.h"
#include "../repo/File_Repo.h"

class Service_Tutorial
{
private:
    Tutorial_Repo repo;
    File_Repo* watchlist;

public:
    ///constructor and destructor
    Service_Tutorial(const Tutorial_Repo &repo,File_Repo* watchlist);

    Service_Tutorial(){}

    ~Service_Tutorial(){}







    /// function that deletes a tutorial
    /// \param title of the tutorial to be deleted
    /// \return 1 if it was deleted or -1 otherwise
    int delete_service(string title);

    /// function that updates a tutorial
    /// \param title of the tutorial to be updated
    /// \param t the new tutorial
    /// \return 1 if it was updated or -1 otherwise
    int update_service(string title, Tutorial t);

    vector<Tutorial> search_by_presenter(string presenter);

    /// get the length of the service
    /// \return
    int get_service_length();

    /// function to return a tutorial on a given position
    /// \param position- the position of the wanted tutorial
    /// \return the tutorial on that position
    Tutorial get_by_position(int position);

    void add_to_watchlist(Tutorial tutorial);

    void delete_from_watchlist(Tutorial tutorial);

    File_Repo* get_watchlist() const {return watchlist;}

    Tutorial_Repo get_repo() const {return repo;}

    void open_app();

    void load_repo();


    int add_service(Tutorial tutorial);
};

