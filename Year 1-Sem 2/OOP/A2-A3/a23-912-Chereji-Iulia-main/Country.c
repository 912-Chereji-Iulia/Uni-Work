//
// Created by Iulia on 03.03.2021.
//
#include "Country.h"
#include <string.h>
#include <stdio.h>
#include <stdlib.h>



Country* createCountry(char* name, char* continent, int population)
{
    Country* c=(Country*)malloc(sizeof(Country));
    if(c==NULL)
        return NULL;

    c->name = (char*)malloc(sizeof(char) * (strlen(name) + 1));
    strcpy(c->name, name);

    c->continent = (char*)malloc(sizeof(char)* (strlen(continent) + 1));
    strcpy(c->continent, continent);

    c->population = population;

    return c;
}

char* get_name(Country* c)
{
    return c->name;
}

char* get_continent(Country* c)
{
    return c->continent;
}

int get_population(Country* c)
{
    return c->population;
}

void to_string(Country* c, char* str)
{
    sprintf(str, "Country: %s - Continent: %s - population: %d\n", get_name(c), get_continent(c), get_population(c));
}

Country* copy_country(Country* c)
{
    Country* new=createCountry(get_name(c), get_continent(c), get_population(c));
    return new;
}

void destroy_country(Country* c)
{
    if(c==NULL)
        return;
    free(c->name);
    free(c->continent);

    free(c);
}



