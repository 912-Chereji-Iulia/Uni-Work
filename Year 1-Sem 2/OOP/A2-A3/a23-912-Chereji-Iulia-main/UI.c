//
// Created by Iulia on 06.03.2021.
//

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "Country-Repo.h"
#include "Service.h"
#include "Country.h"
#include "UI.h"


UI* createUI(CountryService* service)
{
    UI* ui = (UI*)malloc(sizeof(UI));
    ui->service = service;
    return ui;
}

void print_menu()
{
    printf("\n1.Add a country");
    printf("\n2.Delete a country");
    printf("\n3.Update a country");
    printf("\n4.List all countries");
    printf("\n5.Filter the countries by name.");
    printf("\n6.Filter the countries by continent.");
    printf("\n7.Countries on a given continent, sorted ascending by population.");
    printf("\n8.Countries on a given continent, sorted descending by population.");
    printf("\n9.Undo");
    printf("\n10.Redo");
    printf("\n0.Exit\n");
}

int valid_command(int command)
{
    if (command < 0 || command > 10)
        return 0;
    return 1;
}

int valid_continent(char* continent)
{   char Continents[5][10]={"Europe", "Asia","Africa", "America", "Australia"};
    for(int i=0;i<5;i++)
        if(strcmp(continent,Continents[i])==0)
            return 1;
    return 0;
}

int read_int(const char* message)
{
    int ok=0, nr;
    char number[100];
    while(ok==0)
    {
        printf("%s",message);
        scanf("%s",number);
        int successful=sscanf(number,"%d",&nr);
        if(successful==1)
            ok=1;
        if(ok!=1)
            printf("Error reading an int\n");
    }
    return nr;
}

void display_countries(UI* ui)
{
    CountryRepo* repo=get_repo(ui->service);
    int length = get_length(repo);

    if(length==0)
        printf("There are no countries!\n");
    else
    {
        for(int i=0;i<length;i++)
        {   char country[100];
            to_string(get_by_position(repo,i),country);
            printf("%s\n", country);

        }

    }

}


void display_countries_by_name(UI* ui,char* input)
{
    CountryRepo* repo=search_by_name(ui->service,input);

    int length = get_length(repo);

    if(length==0)
        printf("There are no countries!\n");
    else
    {
        for(int i=0;i<length;i++)
        {   char country[100];
            to_string(get_by_position(repo,i),country);
            printf("%s\n", country);

        }
    }
}

void display_sorted_by_name(UI *ui,char*input)
{
    CountryRepo * repo=sort_by_name(ui->service,input);
    int length = get_length(repo);

    if(length==0)
        printf("There are no countries!\n");
    else
    {
        for(int i=0;i<length;i++)
        {   char country[100];
            to_string(get_by_position(repo,i),country);
            printf("%s\n", country);

        }
        destroy_repo(repo);
    }
}

void display_countries_by_continent(UI* ui,char* input)
{
    CountryRepo* repo=search_by_continent(ui->service,input);
    int length = get_length(repo);

    if(length==0)
        printf("There are no countries!\n");
    else
    {
        for(int i=0;i<length;i++)
        {   char country[100];
            to_string(get_by_position(repo,i),country);
            printf("%s\n", country);

        }
        destroy_repo(repo);
    }

}

void display_countries_by_cont_and_population(UI* ui,char* input, int nr)
{
    CountryRepo* repo=sort_by_population(ui->service,nr,input);
    int length = get_length(repo);

    if(length==0)
        printf("There are no countries!\n");
    else
    {
        for(int i=0;i<length;i++)
        {   char country[100];
            to_string(get_by_position(repo,i),country);
            printf("%s\n", country);

        }
        destroy_repo(repo);
    }

}

void display_countries_by_cont_and_population_descending(UI* ui,char* input, int nr)
{
    CountryRepo* repo=sort_by_population_descending(ui->service,nr,input);
    int length = get_length(repo);

    if(length==0)
        printf("There are no countries!\n");
    else
    {
        for(int i=0;i<length;i++)
        {   char country[100];
            to_string(get_by_position(repo,i),country);
            printf("%s\n", country);

        }
        destroy_repo(repo);
    }

}



void destroy_ui(UI* ui)
{
    destroy_service(ui->service);
    free(ui);
}


