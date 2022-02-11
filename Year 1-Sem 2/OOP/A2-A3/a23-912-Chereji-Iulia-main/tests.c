//
// Created by Iulia on 11.03.2021.
//

#include "Country.h"
#include "Country-Repo.h"
#include "Operations-List.h"
#include "Service.h"
#include <assert.h>
#include <string.h>
#include "Array.h"
#include <stdio.h>

void test_country()
{
    Country* c=createCountry("Romania","Europe", 19149832);
    assert(strcmp(c->name, "Romania")==0);
    assert(strcmp(c->continent, "Europe")==0);
    assert(c->population==19149832);
    destroy_country(c);


}

void test_repo()
{
    CountryRepo* repo=createRepo();
    Country* c=createCountry("Romania","Europe", 19149832);
    Country* c1=createCountry("Romania","Europe", 19149834);
    add_country(repo,c);
    assert(strcmp(get_by_position(repo,0)->name, "Romania")==0);
    assert(strcmp(get_by_position(repo,0)->continent, "Europe")==0);
    assert(get_by_position(repo,0)->population==19149832);
    int upd=update_country(repo,c1,"Romania");
    assert(upd==1);
    assert(get_by_position(repo,0)->population==19149834);
    destroy_country(c1);
    destroy_country(c);
    destroy_repo(repo);


}

void test_service()
{
    CountryRepo* repo=createRepo();
    CountryService* service=createService(repo);
    Country* c= createCountry("Romania", "Europe",19149832 );
    int ad=add_service(service,c->name,c->continent,c->population);
    assert(ad==1);

    assert(strcmp(c->name,"Romania")==0);
    assert(strcmp(c->continent,"Europe")==0);
    assert(c->population==19149832);

    int del=delete_service(service,c->name);
    assert(del==1);

    int add=add_country(repo,c);
    Country* c1=createCountry("Romania", "Europe",12345566);
    int add1=add_country(repo,c1);

    assert(update_service(service,c1->name,c1->continent,c1->population,c->name)==1);


    destroy_country(c);
    destroy_country(c1);
    destroy_service(service);


}

void test_op_list()
{
    Op_list* list=create_list();
    Country* c=createCountry("Romania","Europe", 19149832);
    Country* c1=createCountry("Italy","Europe", 23456789);
    Op* o=create_operation(c,"add");
    Op* o1=create_operation(c1,"add");
    Op* o2=create_operation(c,"delete");
    Op* o3=create_operation(c1,"update");

    destroy_country(c);
    destroy_country(c1);

    add_op(list,o);
    add_op(list,o1);
    add_op(list,o2);
    add_op(list,o3);

    destroy_op(o);
    destroy_op(o1);
    destroy_op(o2);
    destroy_op(o3);

    assert(list_empty(list)==0);

    Op* o4=remove_op(list);
    assert(strcmp(o4->op_name,"update")==0);
    destroy_op(o4);

    o4=remove_op(list);
    assert(strcmp(o4->op_name,"delete")==0);
    destroy_op(o4);

    o4=remove_op(list);
    assert(strcmp(o4->op_name,"add")==0);
    destroy_op(o4);

    o4=remove_op(list);
    assert(strcmp(o4->op_name,"add")==0);
    destroy_op(o4);

    assert(list_empty(list)==1);

    destroy_list(list);


}

void test_dyn_array()
{
    DynamicArray* arr=createDynamicArray(10,(DestroyElementFunction )&destroy_country);
    Country* c1=createCountry("Romania","Europe",12345);
    add(arr,c1);
    assert(strcmp(c1->name,"Romania")==0);
    assert(get_elem(arr,0)==c1);
    assert(get_arr_length(arr)==1);
    delete(arr,0);
    assert(get_arr_length(arr)==0);
    destroy(arr);
}

void test_all()
{
    test_country();
    test_repo();
    test_service();
    test_op_list();
    test_dyn_array();
}

