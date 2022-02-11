//
// Created by Iulia on 03.03.2021.
//
#pragma once

typedef struct
{
    char* name;
    char* continent;
    int population;
}Country;

///
/// \param name given for this country
/// \param continent given for this country
/// \param population given for this country
/// \return a country with the given name, continent and population
Country* createCountry(char* name, char* continent, int population);

///
/// \param c the country
/// \return its name
char* get_name(Country* c);

///
/// \param c the country
/// \return its continent
char* get_continent(Country* c);

///
/// \param c the country
/// \return its population
int get_population(Country* c);

///
/// \param c the country to be printed
/// \param str
void to_string(Country* c, char* str);

///
/// \param c the country
/// \return a copy of this country
Country* copy_country(Country* c);

///
/// \param c country to be destroyed
void destroy_country(Country* c);