////
//// Created by Iulia on 08.05.2021.
////
//
//#ifndef A89_912_CHEREJI_IULIA_GUI_H
//#define A89_912_CHEREJI_IULIA_GUI_H
//
//
//#include <QWidget>
//#include "../service/Service.h"
//#include <QtWidgets/qmainwindow.h>
//#include <QtWidgets/qlistwidget.h>
//#include <QtWidgets/qboxlayout.h>
//#include <QtWidgets/qlineedit.h>
//#include <QtWidgets/qformlayout.h>
//#include <QtWidgets/qlabel.h>
//#include <QtWidgets/qpushbutton.h>
//#include <QtWidgets/qradiobutton.h>
//#include <QtWidgets/qmessagebox.h>
//#include <QtWidgets/qbuttongroup.h>
//
//class GUI: public QWidget{
//
//    Q_OBJECT
//
//private:
//    Service_Tutorial service;
//
//
//
//    std::vector<Tutorial> list_tutorials;
//    QListWidget * list_of_tutorials_widget;
//    QListWidget *watchList;
//
//    QPushButton* addButton;
//    QPushButton* deleteButton;
//    QPushButton* updateButton;
//    QPushButton* add_to_watchlist_button;
//    QPushButton* nextButton;
//    QPushButton* add_to_watchlist_Button;
//    QPushButton* removeButton;
//    QPushButton* admin;
//    QPushButton* user;
//
//
//    QLineEdit* title;
//    QLineEdit* presenter;
//    QLineEdit* likes;
//    QLineEdit* duration;
//    QLineEdit* link;
//
//
//public:
//
//    GUI(){}
//    ~GUI(){}
//    GUI(Service_Tutorial& service, QWidget* parent =0);
//
//    void main_window();
//
//    void add_list_of_tutorials();
//
//    void add_watchlist();
//
//    void connect_signals_slots();
//
//    void first_window();
//
//
//    QWidget *admin_window();
//
//    void add_new_tutorial();
//
//    int get_selected_tutorial_index();
//};
//
//
//#endif //A89_912_CHEREJI_IULIA_GUI_H
