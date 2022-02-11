//
// Created by Iulia on 18.03.2021.
//
#pragma once
#include "../domain/Dyn-Array.h"
#include "../validators/Validator.h"
#include <vector>

class Tutorial_Repo
{
private:
    vector<Tutorial> tutorials;
    string file_name;

public:
    /// constructor and destructor
    Tutorial_Repo()= default;

    Tutorial_Repo(const string &file_name);

    ~Tutorial_Repo()= default;


    vector<Tutorial> get_all() {return tutorials;}

    /// function to add a tutorial to the repo
    /// \param tutorial - tutorial to be added
    /// \return 1 if the tutorial was added and -1 otherwise (if the tutorial is already in the repo)
     int add_tutorial( Tutorial& tutorial);

    /// function to delete a tutorial from the repo
    /// \param title - title of the tutorial to be deleted
    /// \return 1 if it was deleted or -1 otherwise
     int delete_tutorial(string title);



    /// function to update a tutorial from the repo
    /// \param title-title of the tutorial to be updated
    /// \param new_tutorial - the new tutorial
    /// \return 1 if it was successfully updated or -1 if the tutorial isn't in the repo
     int update_tutorial(string title, Tutorial new_tutorial);

    /// function that gets the length of the repo
    /// \return
    int get_repo_length();

    /// function that returns the tutorial on a given position
    /// \param position - the position of the wanted tutorial
    /// \return the tutorial
    Tutorial get_by_pos_repo(int position);


    vector<Tutorial> search_by_presenter(string presenter);

    void save();

    void load();


};

