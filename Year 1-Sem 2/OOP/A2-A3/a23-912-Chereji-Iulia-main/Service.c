//
// Created by Iulia on 06.03.2021.
//
#include "Service.h"
#include <stdlib.h>
#include <string.h>
#include "Country-Repo.h"
#include "Operations-List.h"
#include <stdio.h>

CountryService* createService(CountryRepo* repo)
{
    CountryService* service= (CountryService*)malloc(sizeof(CountryService));
    service->repo=repo;
    service->undo=create_list();
    service->redo=create_list();
    service->possible=1;
    return service;
}


int add_service(CountryService* service, char* name, char* continent, int population)
{
    Country * c=createCountry(name,continent,population);
    int added=add_country(service->repo, c);
    if(added==1 && service->possible)
    {
        Op* op=create_operation(c,"add");
        add_op(service->undo,op);
        destroy_op(op);
    }
    destroy_country(c);
    return added;

}

int delete_service(CountryService* service, char* name)
{   int pos=find_country(service->repo,name);
    if(pos==-1)
    {
        return 0;
    }
    else
    {   Country* c=copy_country(get_by_position(service->repo,pos));
        int deleted=delete_country(service->repo, name);

        if(deleted && service->possible)
        {

            Op* op=create_operation(c,"delete");
            add_op(service->undo,op);
            destroy_op(op);
        }
        destroy_country(c);
        return deleted;}
}

int update_service(CountryService* service, char* name, char* continent, int population, char* old_name)
{
    Country* new=createCountry(name, continent, population);
    int pos=find_country(service->repo, old_name);
    Country* old=copy_country(get_by_position(service->repo,pos));
    int updated=update_country(service->repo, new, old_name);
    if(updated==1 && service->possible)
    {

        Op* op=create_operation(new,"update");
        add_op(service->undo,op);
        destroy_op(op);
        Op* old_op=create_operation(old,"update");
        add_op(service->undo,old_op);
        destroy_op(old_op);
    }
    destroy_country(old);
    destroy_country(new);
    return updated;
}





CountryRepo* search_by_name(CountryService* service, char* name)
{
    CountryRepo* new_repo=createRepo();
    for(int i=0;i<get_length(service->repo);i++)
    {
        Country* c=get_by_position(service->repo,i);
        if (strstr(get_name(c),name))
            add_country(new_repo,c);
    }
    return new_repo;
}

CountryRepo* sort_by_name(CountryService* service,char *input)
{
    int j;
    CountryRepo* new_repo=search_by_name(service,input);
    for(int i=0;i<get_length(new_repo)-1;i++)
    {
        for ( j = i+1; j <get_length(new_repo) ; j++) {
            Country* c1=get_by_position(new_repo, i);
            Country* c2=get_by_position(new_repo, j);
            if(strcmp(c1->name,c2->name)>0)
            {
                Country* aux=c1;
                new_repo->countries->elems[i]=new_repo->countries->elems[j];
                new_repo->countries->elems[j]=aux;
            }
        }}
    return new_repo;
}

CountryRepo* search_by_population_and_cont(CountryService* service, int input,char *cont)
{
    CountryRepo* new_repo=createRepo();
    for(int i=0;i<get_length(service->repo);i++)
    {
        Country* c=get_by_position(service->repo,i);
        if (c->population > input && strstr(c->continent,cont))
            add_country(new_repo,c);
    }
    return new_repo;
}


CountryRepo* sort_by_population(CountryService* service,int input, char*cont)
{
    CountryRepo* new_repo=search_by_population_and_cont(service,input,cont);
    for(int i=0;i<get_length(new_repo)-1;i++)
    {
        for (int j = i+1; j <get_length(new_repo) ; j++) {
            Country* c1=get_by_position(new_repo, i);
            Country* c2=get_by_position(new_repo, j);
            if(c1->population>c2->population)
            {
                Country* aux=c1;
                new_repo->countries->elems[i]=new_repo->countries->elems[j];
                new_repo->countries->elems[j]=aux;
            }
        }}
    return new_repo;
}

CountryRepo* sort_by_population_descending(CountryService* service,int input, char*cont)
{
    CountryRepo* new_repo=search_by_population_and_cont(service,input,cont);
    for(int i=0;i<get_length(new_repo)-1;i++)
    {
        for (int j = i+1; j <get_length(new_repo) ; j++) {
            Country* c1=get_by_position(new_repo, i);
            Country* c2=get_by_position(new_repo, j);
            if(c1->population<c2->population)
            {
                Country* aux=c1;
                new_repo->countries->elems[i]=new_repo->countries->elems[j];
                new_repo->countries->elems[j]=aux;
            }
        }}
    return new_repo;
}



CountryRepo* search_by_continent(CountryService* service, char* continent)
{
    CountryRepo* new_repo=createRepo();
    for(int i=0;i<get_length(service->repo);i++)
    {
        Country* c=get_by_position(service->repo,i);
        if (strstr(get_continent(c),continent))
            add_country(new_repo,c);
    }
    return new_repo;
}

CountryRepo* get_repo(CountryService* service)
{
    return service->repo;
}

void migrate_service(CountryService* service, Country* initial_country, Country* final_country, int nr_of_people)
{   Country* init=copy_country(initial_country);
    Op* op=create_operation(init,"migrate");
    add_op(service->undo,op);
    destroy_op(op);

    Country* fin=copy_country(final_country);
    Op* op1=create_operation(fin,"migrate");
    add_op(service->undo,op1);
    destroy_op(op1);
    migration(service->repo, initial_country, final_country, nr_of_people);
    if(service->possible)
    {
        Op* op=create_operation(initial_country,"migrate");
        add_op(service->undo,op);
        destroy_op(op);
        Op* op1=create_operation(final_country,"migrate");
        add_op(service->undo,op1);
        destroy_op(op1);
    }
    destroy_country(init);
    destroy_country(fin);

}
int undo_op(CountryService* service)
{
    if(list_empty(service->undo))
        return 0;
    Op* op=remove_op(service->undo);
    if(strcmp(get_op_name(op),"add")==0)
    {
        Country* c=get_country(op);
        Op* o=create_operation(c,"add");
        add_op(service->redo,o);
        destroy_op(o);
        delete_country(service->repo,get_name(c));

    }
    else
    {
        if(strcmp(get_op_name(op),"delete")==0)
        {
            Country* c=get_country(op);
            Op* o=create_operation(c,"delete");
            add_op(service->redo,o);
            add_country(service->repo,c);
            destroy_op(o);
        }
        else
        {
            if(strcmp(get_op_name(op),"update")==0)
            {
                Op* o=remove_op(service->undo);
                Country* new=get_country(o);
                Country* old=get_country(op);
                update_country(service->repo,old,new->name);

                add_op(service->redo,op);
                add_op(service->redo,o);
                destroy_op(o);
            }
            else if (strcmp(get_op_name(op),"migrate")==0)
            {
                Country* fin=get_country(op);
                int nr_fin=fin->population;
                Op* init=remove_op(service->undo);
                Country* ini=get_country(init);
                Op* fin_init=remove_op(service->undo);
                Country* fin_initial=get_country(fin_init);
                int nr_fin_init=fin_initial->population;
                int migrants=nr_fin-nr_fin_init;


                update_service(service,fin_initial->name,fin_initial->continent,fin_initial->population,fin_initial->name);
                update_service(service,ini->name, ini->continent,ini->population+migrants,ini->name);
                add_op(service->redo,fin_init);
                add_op(service->redo,init);
                add_op(service->redo,op);
                destroy_op(fin_init);
                destroy_op(init);

            }


        }

    }
    destroy_op(op);
    service->possible=1;
    return 1;
}

int redo_op(CountryService* service)
{
    if(list_empty(service->redo))
        return 0;
    Op* op=remove_op(service->redo);
    service->possible=0;
    if(strcmp(get_op_name(op),"add")==0)
    {
        Country* c=get_country(op);
        add_service(service,c->name,c->continent,c->population);

    }
    else
    {
        if(strcmp(get_op_name(op),"delete")==0)
        {
            Country* c=get_country(op);
            delete_service(service,get_name(c));
        }
        else
        {
            if(strcmp(get_op_name(op),"update")==0)
            {
                Op* o=remove_op(service->redo);
                Country* new=get_country(op);
                Country* old=get_country(o);
                update_service(service,new->name,new->continent,new->population,old->name);

                destroy_op(o);

            }
            else if(strcmp(get_op_name(op),"migrate")==0)
            {
                Country* fin=get_country(op);
                int nr_fin=fin->population;
                Op* init=remove_op(service->redo);
                Country* ini=get_country(init);

                Op* fin_init=remove_op(service->redo);
                Country* fin_initial=get_country(fin_init);
                int nr_fin_init=fin_initial->population;

                int migrants=nr_fin-nr_fin_init;
                update_service(service,fin_initial->name,fin_initial->continent,fin_initial->population+migrants,fin_initial->name);
                update_service(service,ini->name, ini->continent,ini->population,ini->name);
                destroy_op(fin_init);
                destroy_op(init);

            }
        }

    }
    destroy_op(op);
    service->possible=1;
    return 1;
}

void destroy_service(CountryService* service)
{
    destroy_repo(service->repo);
    destroy_list(service->undo);
    destroy_list(service->redo);
    free(service);
}