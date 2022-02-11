//
// Created by Iulia on 06.03.2021.
//
#include "Country-Repo.h"
#include "Array.h"
#include "Country.h"
#include <stdlib.h>
#include <string.h>


CountryRepo* createRepo()
{
    CountryRepo* repo =(CountryRepo*)malloc(sizeof(CountryRepo));
    repo->countries = createDynamicArray(cap,(DestroyElementFunction) &destroy_country);
    return repo;
}

int add_country(CountryRepo* repo, Country* c)
{

    if(repo==NULL)
        return 0;
    int pos=find_country(repo,c->name);
    if(pos !=-1)
    {
        return 0;
    }
    Country* copy=copy_country(c);
    add(repo->countries, copy);

    return 1;
}

int find_country(CountryRepo* repo, char* name)
{

    if(repo==NULL)
        return -1;

    for(int i=0;i<get_arr_length(repo->countries);i++)
    {
        Country* c=get_elem(repo->countries, i);
        if(strcmp(c->name,name)==0)
            return i;
    }
    return -1;
}


int delete_country(CountryRepo* repo, char* name)
{  if (repo == NULL)
        return 0;
   int p=find_country(repo,name);
   if (p==-1)
      return 0;
   delete(repo->countries,p);
   return 1;
}

int update_country(CountryRepo* repo, Country* new, char* old_name)
{
    if (repo == NULL)
        return -1;
    int p=find_country(repo,old_name);
    if(p==-1)
        return 0;
    delete_country(repo,old_name);
    add_country(repo,new);
    return 1;
}

void migration(CountryRepo* repo, Country* initial_country, Country* final_country, int nr_of_people)
{

    initial_country->population -= nr_of_people;
    final_country->population +=nr_of_people;

}

Country* get_by_position(CountryRepo* repo, int position)
{
    if(repo==NULL ||position<0 || position>get_length(repo))
        return NULL;
    return get_elem(repo->countries, position);
}


int get_length(CountryRepo* repo)
{
    return get_arr_length(repo->countries);
}

void destroy_repo(CountryRepo* repo)
{
    if(repo==NULL)
        return;
    destroy(repo->countries);
    free(repo);
}

