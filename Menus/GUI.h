//
// Created by Iulia on 08.05.2021.
//

#ifndef A89_912_CHEREJI_IULIA_GUI_H
#define A89_912_CHEREJI_IULIA_GUI_H


#include <QWidget>
#include "../service/Service.h"
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

class GUI: public QWidget{

Q_OBJECT



private:
    Service_Tutorial service;

    QPushButton* admin;
    QPushButton* user;
    QRadioButton* html;
    QRadioButton* csv;

    QButtonGroup* radio_buttons;

public:


    GUI(Service_Tutorial& service, QWidget* parent=nullptr);
    GUI(QWidget *parent);
    void connect_signals_slots();

    void first_window();


    void admin_mode();

    void user_mode();

    void html_csv(QHBoxLayout *html_csv_layout);

    void csv_save();

    void html_save();
};


#endif //A89_912_CHEREJI_IULIA_GUI_H
