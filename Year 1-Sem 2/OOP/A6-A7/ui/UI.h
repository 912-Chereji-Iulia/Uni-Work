//
// Created by Iulia on 18.03.2021.
//

#pragma once
# include "../service/Service.h"

class UI
{
private:
    Service_Tutorial service;

public:
    ///constructor and destructor
    UI(){}
    ~UI(){}
    UI(Service_Tutorial& service);


    ///the load_repo function
    void start_me();

    ///function to print the general menu
    void print_general_menu();

    ///function to print the admin menu
    void print_admin_menu();

    ///function to print the user menu
    void print_user_menu();

    ///add function for the UI
    void add_tutorial_ui();

    ///delete function for the UI
    void  delete_tutorial_ui();

    ///update function for the UI
    void update_tutorial_ui();

    ///function to list all tutorials
    void display_all();

    void display_by_presenter();

    void add_to_watchlist( Tutorial t);

    ///the 10 entries at the beginning of the program
    void start_entries();


    void display_watchlist();

    void delete_from_watchlist();


    void open_app();
};