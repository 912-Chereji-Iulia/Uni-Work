//
// Created by Iulia on 13.05.2021.
//

#include "GUI.h"
#include "../Menus/ADMIN.h"
#include "ADMIN.h"
#include "USER.h"
#include "../repo/HTML.h"
#include "../repo/CSV.h"


GUI::GUI( QWidget *parent): QWidget{parent}{

    this->html_save();
    this->csv_save();
   // this->service=service;
    this->first_window();
    this->connect_signals_slots();

}

void GUI::first_window() {
    this->setWindowTitle("Master C++ - Admin or user?");
    QVBoxLayout* first_dialog_window=new QVBoxLayout{ this};
    QLabel* main_title=new QLabel{"Welcome to Master C++!" };
    QFont font("Itim", 20, 20, true);
    main_title->setStyleSheet("background-color:orange;");
    main_title->setFont(font);
    main_title->setAlignment(Qt::AlignCenter);
    first_dialog_window->addWidget(main_title);

    QWidget* first_widget = new QWidget{};
    QHBoxLayout* first_layout = new QHBoxLayout{first_widget};

    QGridLayout* grid_layout = new QGridLayout{};
    this->admin = new QPushButton("Admin mode");
    this->user = new QPushButton("User mode");


    grid_layout->addWidget(admin, 0, 0);
    grid_layout->addWidget(user, 1, 0);



    QWidget* buttons_widget = new QWidget{};
    buttons_widget->setLayout(grid_layout);
    first_layout->addWidget(buttons_widget);
    first_dialog_window->addWidget(first_widget);

    QHBoxLayout* html_csv_layout=new QHBoxLayout{};
    this->html_csv(html_csv_layout);
    first_dialog_window->addLayout(html_csv_layout);


}

void GUI::html_csv(QHBoxLayout* html_csv_layout){

    this->radio_buttons=new QButtonGroup{};
    this->html=new QRadioButton{"HTML"};
    this->radio_buttons->addButton(this->html);
    this->csv=new QRadioButton{"CSV"};
    this->radio_buttons->addButton(this->csv);
    this->radio_buttons->setExclusive(true);
    html_csv_layout->addWidget(new QLabel{"Choose a mode to save the watchlist: "});
    html_csv_layout->addWidget(this->html);
    html_csv_layout->addWidget(this->csv);

}

void GUI::connect_signals_slots() {
    QObject::connect(this->admin,&QPushButton::clicked, this, &GUI:: admin_mode);
    QObject::connect(this->user,&QPushButton::clicked, this, &GUI:: user_mode);
    QObject::connect(this->html,&QRadioButton::clicked, this, &GUI:: html_save);
    QObject::connect(this->csv,&QRadioButton::clicked, this, &GUI:: csv_save);
}


void GUI::html_save(){
    File_Repo* watchlist=new HTML("watchlist.html");
    Tutorial_Repo repo("t1.txt");
    Service_Tutorial service{repo,watchlist};
    this->service=service;
}

void GUI::csv_save(){
    File_Repo* watchlist=new CSV("watchlist.csv");
    Tutorial_Repo repo("t1.txt");
    Service_Tutorial service{repo,watchlist};
    this->service=service;
}
void GUI::admin_mode()
{
    this->hide();
    ADMIN* admin_menu=new ADMIN{this, this->service};
    admin_menu->show();


}

void GUI::user_mode()
{
    this->hide();
    USER* user_menu=new USER{this,this->service};
    user_menu->show();

}