//
// Created by Iulia on 06.03.2021.
//
#pragma once

typedef struct {
    CountryService* service;
}UI;
UI* createUI(CountryService* c);
void print_menu();
int valid_command(int command);
int read_int(const char* message);
int valid_continent(char* continent);
void display_countries(UI* ui);
void display_countries_by_name(UI* ui, char* input);
void display_countries_by_continent(UI* ui,char* input);
void display_sorted_by_name(UI *ui,char*input);
void display_countries_by_cont_and_population(UI* ui,char* input, int nr);
void display_countries_by_cont_and_population_descending(UI* ui,char* input, int nr);
void destroy_ui(UI* ui);