//
// Created by Iulia on 08.05.2021.
//

#ifndef A89_912_CHEREJI_IULIA_USER_H
#define A89_912_CHEREJI_IULIA_USER_H


#include <QWidget>
#include "../service/Service.h"
#include "GUI.h"
#include <QtWidgets/qmainwindow.h>
#include <QtWidgets/qlistwidget.h>
#include <QtWidgets/qboxlayout.h>
#include <QtWidgets/qlineedit.h>
#include <QtWidgets/qformlayout.h>
#include <QtWidgets/qlabel.h>
#include <QtWidgets/qpushbutton.h>
#include <QtWidgets/qradiobutton.h>
#include <QtWidgets/qmessagebox.h>
#include <QtWidgets/qbuttongroup.h>

class USER: public QWidget{

    Q_OBJECT

private:
    Service_Tutorial service;
    GUI* gui;



    std::vector<Tutorial> list_tutorials;
    std::vector<Tutorial>*  watchlist;
    QListWidget * list_of_tutorials_widget;
    QListWidget *watchList;
    QListWidget *list_by_presenter;
    QLineEdit* presenter;


    QPushButton* filterButton;
    QPushButton* nextButton;
    QPushButton* add_to_watchlist_Button;
    QPushButton* removeButton;
    QPushButton* playButton;
    QPushButton* openButton;




public:


    USER(GUI* gui,Service_Tutorial& service, QWidget* parent =0);

    void main_window();

    void add_to_watchlist();

    void connect_signals_slots();

    void html_csv(QVBoxLayout *html_csv_layout);

    void closeEvent(QCloseEvent *event);

    void display_by_presenter();

    void filter_by_presenter();

    void display_watchlist();

    int get_selected_tutorial_index();

    void delete_from_watchlist();

    int get_selected_tutorial_index_watchlist();

    void next_tutorial_watchlist();

    void play_tutorial();

    void open_watchlist();
};


#endif //A89_912_CHEREJI_IULIA_USER_H
