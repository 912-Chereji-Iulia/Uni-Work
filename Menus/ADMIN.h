//
// Created by Iulia on 08.05.2021.
//

#ifndef A89_912_CHEREJI_IULIA_ADMIN_H
#define A89_912_CHEREJI_IULIA_ADMIN_H


#include <QWidget>
#include "../service/Service.h"
#include "../Menus/GUI.h"
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



class ADMIN: public QWidget{

Q_OBJECT

private:
    Service_Tutorial service;
    GUI* gui;

    std::vector<Tutorial> list_tutorials;
    QListWidget * list_of_tutorials_widget;
    QListWidget *watchList;
    QListView* list_view;

    QPushButton* addButton;
    QPushButton* deleteButton;
    QPushButton* updateButton;



    QLineEdit* title;
    QLineEdit* title_delete;
    QLineEdit* title_update;
    QLineEdit* new_title;
    QLineEdit* presenter;
    QLineEdit* likes;
    QLineEdit* duration;
    QLineEdit* link;
    QLineEdit* new_presenter;
    QLineEdit* new_likes;
    QLineEdit* new_duration;
    QLineEdit* new_link;


public:

    ADMIN(GUI* gui, Service_Tutorial& service, QWidget* parent=nullptr );

    void main_window() ;


    void add_list_of_tutorials() ;

    void connect_signals_slots() ;

    void add_new_tutorial() ;

    void delete_tutorial();

   void update_tutorial();

    void exit_admin_mode(QCloseEvent *mode);

    void closeEvent(QCloseEvent *event);
};


#endif //A89_912_CHEREJI_IULIA_ADMIN_H
