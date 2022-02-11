//
// Created by Iulia on 06.03.2021.
//

#pragma once

#include "Country-Repo.h"
#include "Operations-List.h"
typedef struct {
    CountryRepo* repo;
    Op_list* undo,*redo;
    int possible;


}CountryService;

/// function that creates the service
/// \param repo the repository
/// \return the service
CountryService* createService(CountryRepo* repo);

/// function that adds a country to the service
/// \param service the service
/// \param name of the new country
/// \param continent of the new country
/// \param population of the new country
/// \return 1 if it was successfully added or 0 otherwise(if it already exists)
int add_service(CountryService* service, char *name, char* continent, int population);

/// function that deletes a country from the service
/// \param service
/// \param name of the country to be deleted
/// \return 1 if it was successfully deleted or 0 if it wasn't in the repo
int delete_service(CountryService* service, char* name);

/// function that updates a country to the service
/// \param service
/// \param name of the new country
/// \param continent of the new country
/// \param population of the new country
/// \param old_name of the country to be updated
/// \return
int update_service(CountryService* service, char* name, char* continent, int population, char* old_name);

/// function that searches all countries that contain a given string in their name
/// \param service
/// \param name the string
/// \return a repo with all those countries
CountryRepo* search_by_name(CountryService* service, char* name);

/// function that searches all countries that contain a given string in their continent
/// \param service
/// \param continent the string
/// \return a repo with all those countries
CountryRepo* search_by_continent(CountryService* service, char* continent);

///
/// \param service
/// \return the repo
CountryRepo* get_repo(CountryService* service);

/// function that manages the migrations
/// \param service
/// \param initial_country from where they migrate
/// \param final_country to where they migrate
/// \param nr_of_people how many people migrate
void migrate_service(CountryService* service, Country* initial_country, Country* final_country, int nr_of_people);

/// function that sorts a repo by name,in ascending order
/// \param service
/// \param input the string by which we search the countries by name
/// \return sorted repo
CountryRepo* sort_by_name(CountryService* service,char *input);

/// function that searches in a repo countries by population and continent
/// \param service
/// \param input the minimum nr of people that should be
/// \param cont the string by which we search the countries by continent
/// \return
CountryRepo* search_by_population_and_cont(CountryService* service, int input,char *cont);

/// function that sorts a repo by population and continent,in ascending order
/// \param service
/// \param input the minimum nr of people that should be
/// \param cont the string by which we search the countries by continent
/// \return sorted repo
CountryRepo* sort_by_population(CountryService* service,int input, char*cont);

/// function that sorts a repo by population and continent,in descending order
/// \param service
/// \param input the minimum nr of people that should be
/// \param cont the string by which we search the countries by continent
/// \return sorted repo
CountryRepo* sort_by_population_descending(CountryService* service,int input, char*cont);

/// undo operation
/// \param service
/// \return 1 it the undo was done successfully or 0 if there are no more undos
int undo_op(CountryService* service);

/// redo operation
/// \param service
/// \return 1 it the redo was done successfully or 0 if there are no more redos
int redo_op(CountryService* service);

/// function to destroy the service
/// \param service
void destroy_service(CountryService* service);
