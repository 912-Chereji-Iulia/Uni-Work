//
// Created by Iulia on 05.03.2021.
//
#include "Country-Repo.h"
#include "Service.h"
#include "UI.h"
#include "Country.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "tests.h"
#include <crtdbg.h>

int main()
{
    test_all();
    CountryRepo* repo=createRepo();
    Country* c1=createCountry("Romania", "Europe", 20000000);
    add_country(repo,c1);
    Country* c2=createCountry("Hungary", "Europe", 10000000);
    add_country(repo,c2);
    Country* c3=createCountry("Bulgaria", "Europe", 1500000);
    add_country(repo,c3);
    Country* c4=createCountry("China", "Asia", 1439323776);
    add_country(repo,c4);
    Country* c5=createCountry("Spain", "Europe", 46756216);
    add_country(repo,c5);
    Country* c6=createCountry("Greece", "Europe", 10423054);
    add_country(repo,c6);
    Country* c7=createCountry("New Zealand", "Australia", 4822233);
    add_country(repo,c7);
    Country* c8=createCountry("Canada", "America", 37742154);
    add_country(repo,c8);
    Country* c9=createCountry("France", "Europe", 67063703);
    add_country(repo,c9);
    Country* c10=createCountry("Tunis", "Africa", 11818619);
    add_country(repo,c10);

    CountryService* service=createService(repo);
    UI* ui=createUI(service);

    int done=1;
    while (done==1)
    {
        print_menu();
        int input;
        input=read_int("Please enter a command>>> ");
        if(valid_command(input)==0)
            printf("Invalid command");
        else
        {
            if (input==1)
            {   char name[100], continent[100];
                int population,ok=0;
                printf("Enter the name of the country: ");
                scanf("%s", &name);

                while(ok==0) {
                    printf("Enter the name of the continent: ");
                    scanf("%s", &continent);
                    if (valid_continent(continent) == 0)
                        printf("Invalid continent\n");
                    else ok=1;
                }

                population=read_int("Enter the population of the country: ");
                int added=add_service(service,name,continent,population);
                if(added==0)
                    printf("\nThis country already exists!\n");
                else
                    printf("\nAdded\n");

            }

            else
            {
                if (input==0)
                {
                    printf("Bye bye!\n  ");
                    destroy_ui(ui);
                    done=0;
                }
                else
                {
                    if(input==4)
                        display_countries(ui);
                    else
                    {
                        if(input==2)
                        {   char name[200];
                            printf("Enter the name of the country that you want to delete: ");
                            scanf("%s", &name);
                            int res=delete_service(service,name);
                            if(res==0)
                                printf("The country with this name doesn't exist");
                        }
                        else
                        {
                            if(input==3)
                            {
                                char name[200],name1[200],continent[200];
                                int population,ok=0,option;
                                option=read_int("1)Update a country \n 2)manage migration?\n");
                                if(option==1) {
                                    printf("Enter the name of the country that you want to update: ");
                                    scanf("%s", &name);
                                    if (find_country(service->repo, name) == -1)
                                        printf("The country with this name doesn't exist");
                                    else {
                                        printf("Enter the new name of the country: ");
                                        scanf("%s", &name1);

                                        while (ok == 0) {
                                            printf("Enter the new name of the continent: ");
                                            scanf("%s", &continent);
                                            if (valid_continent(continent) == 0)
                                                printf("Invalid continent\n");
                                            else ok = 1;
                                        }

                                        population=read_int("Enter the new population: ");

                                        int res = update_service(service, name1, continent, population, name);
                                        if (res != 1)
                                            printf("The country with this name doesn't exist");

                                    }
                                }
                                else
                                {   char in_name[100], fin_name[100],nr_of_migrants,cont[100];
                                    int pop;
                                    printf("Enter the initial country's name: ");
                                    scanf("%s", &in_name);
                                    int p=find_country(ui->service->repo, in_name);
                                    if(p==-1) {
                                        printf("This country doesn't exist\n Enter its continent: ");
                                        scanf("%s", &cont);
                                        pop=read_int("Enter its population: ");
                                        int added=add_service(ui->service,in_name,cont,pop);
                                        Country* new=get_by_position(ui->service->repo, get_length(ui->service->repo)-1);
                                        printf("Enter the final country's name: ");
                                        scanf("%s", &fin_name);
                                        int p1=find_country(ui->service->repo, fin_name);
                                        Country *final_country = get_by_position(ui->service->repo, p1);
                                        nr_of_migrants=read_int("Enter the nr of migrants: ");
                                        migrate_service(ui->service,new,final_country,nr_of_migrants);
                                        printf("added");
                                    }
                                    else
                                    {
                                        Country* initial_country=get_by_position(ui->service->repo,p);
                                        printf("Enter the final country's name: ");
                                        scanf("%s", &fin_name);
                                        int p1=find_country(ui->service->repo, fin_name);
                                        if(p1==-1)
                                        {   printf("This country doesn't exist\n Enter its continent: ");
                                            scanf("%s", &cont);
                                            pop=read_int("Enter its population: ");

                                            int added=add_service(ui->service,fin_name,cont,pop);
                                            Country* new=get_by_position(ui->service->repo, get_length(ui->service->repo)-1);
                                            nr_of_migrants=read_int("Enter the nr of migrants: ");
                                            migrate_service(ui->service,initial_country,new,nr_of_migrants);


                                        }
                                        else {
                                            Country *final_country = get_by_position(ui->service->repo, p1);
                                            nr_of_migrants=read_int("Enter the nr of migrants: ");
                                            migrate_service(ui->service, initial_country, final_country,
                                                            nr_of_migrants);

                                        }
                                    }



                                }


                            }
                            else
                            {
                                if(input==5)
                                {   char input_name[1000];
                                    getchar();
                                    printf("Enter a string: ");

                                    gets_s(input_name,1000);
                                    if (strlen(input_name)==0)
                                        display_countries(ui);
                                    else
                                    {
                                        display_sorted_by_name(ui,input_name);
                                    }
                                }


                                else
                                {
                                    if(input==6)
                                    {char input_name[1000];
                                        getchar();
                                        printf("Enter a string: ");
                                        gets_s(input_name,1000);
                                        if (strlen(input_name)==0)
                                            display_countries(ui);
                                        else
                                        {   display_countries_by_continent(ui,input_name);

                                        }

                                    }
                                    else
                                    {
                                        if(input==7)
                                        {
                                            char input_name[1000];
                                            printf("Enter a continent: ");
                                            getchar();
                                            gets_s(input_name,1000);
                                            if (strlen(input_name)==0)
                                                display_countries(ui);
                                            else
                                            {   int nr;
                                                nr=read_int("Enter a nr: ");
                                                display_countries_by_cont_and_population(ui,input_name,nr);
                                            }

                                        }
                                        else
                                        {
                                            if(input==8) {
                                                char input_name[1000];
                                                printf("Enter a continent: ");
                                                getchar();
                                                gets_s(input_name, 1000);
                                                if (strlen(input_name) == 0)
                                                    display_countries(ui);
                                                else {
                                                    int nr;
                                                    nr=read_int("Enter a nr: ");
                                                    display_countries_by_cont_and_population_descending(ui,
                                                                                                        input_name,
                                                                                                        nr);
                                                }
                                            }
                                            else
                                            {
                                                if(input==9)
                                                {

                                                    int result=undo_op(ui->service);

                                                    if(result==1)
                                                        printf("Successful undo\n");
                                                    else
                                                        printf("No more undos\n");

                                                }
                                                else
                                                {
                                                    if(input==10)
                                                    {
                                                        int result=redo_op(ui->service);

                                                        if(result==1)
                                                            printf("Successful redo\n");
                                                        else
                                                            printf("No more redos\n");
                                                    }
                                                }
                                            }

                                        }
                                    }

                                }


                            }


                        }
                    }
                }
            }

        }
    }


    destroy_country(c1);
    destroy_country(c2);
    destroy_country(c3);
    destroy_country(c4);
    destroy_country(c5);
    destroy_country(c6);
    destroy_country(c7);
    destroy_country(c8);
    destroy_country(c9);
    destroy_country(c10);
    printf("Are there memory leaks?  %d ",_CrtDumpMemoryLeaks());

    return 0;
}