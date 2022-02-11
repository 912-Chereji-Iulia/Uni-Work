//
// Created by Iulia on 06.03.2021.
//

#pragma once
#include "Array.h"
#include "Country.h"

typedef struct {
    DynamicArray* countries;

}CountryRepo;

///
/// \return the repo created
CountryRepo* createRepo();

/// function to search for the position of a country
/// \param repo the repositry
/// \param name the name of the country
/// \return its position if it is in the repo or -1 otherwise
int find_country(CountryRepo* repo, char* name);

/// function to add a country to the repo
/// \param repo the repository
/// \param c the country to be added
/// \return 1 if it was successfully added or 0 otherwise(if it already exists)
int add_country(CountryRepo* repo, Country* c);

/// function to delete a country of the repo
/// \param repo the repository
/// \param name the name of the country to be deleted
/// \return 1 if it was successfully deleted or 0 if it wasn't in the repo
int delete_country(CountryRepo* repo, char* name);

/// function to update a country of the repo
/// \param repo the repository
/// \param new the new country
/// \param old_name old name of the country to be updated
/// \return 1 if it was successfully updated or 0 if it wasn't in the repo
int update_country(CountryRepo* repo, Country* new, char* old_name);

/// function that gets the length of the repo
/// \param repo the repository
/// \return the length
int get_length(CountryRepo* repo);

/// function that returns a country on a given position
/// \param repo the repository
/// \param position the given position
/// \return the country on that position
Country* get_by_position(CountryRepo* repo, int position);

/// function that manages the migrations
/// \param repo the repository
/// \param initial_country from where they migrate
/// \param final_country to where they migrate
/// \param nr_of_people how many people migrate
void migration(CountryRepo* repo, Country* initial_country, Country* final_country, int nr_of_people);

/// function that destroys the repo
/// \param repo the repository
void destroy_repo(CountryRepo* repo);
