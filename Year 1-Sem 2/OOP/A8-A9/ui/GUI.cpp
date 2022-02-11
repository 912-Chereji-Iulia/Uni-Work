////
//// Created by Iulia on 08.05.2021.
////
//
//#include <QPushButton>
//#include <QApplication>
//#include <QHBoxLayout>
//#include <QListWidget>
//#include <QLabel>
//#include <QFormLayout>
//#include <iostream>
//#include <sstream>
//#include "GUI.h"
//
//GUI::GUI(Service_Tutorial &service, QWidget *parent):service(service), QWidget(parent) {
//
//    //this->first_window();
//    this->main_window();
//    this->list_tutorials= this->service.get_repo().get_all();
//    this->add_list_of_tutorials();
//
//
//
//}
//
//
//void GUI::first_window()
//{
//    this->setWindowTitle("Master C++ - Admin or user?");
//    QVBoxLayout* first_dialog_window=new QVBoxLayout{ this};
//    QLabel* main_title=new QLabel{"Welcome to Master C++!" };
//    QFont font("Itim", 20, 20, true);
//    main_title->setStyleSheet("background-color:lightgreen;");
//    main_title->setFont(font);
//    first_dialog_window->addWidget(main_title);
//
//    QWidget* first_widget = new QWidget{};
//    QHBoxLayout* first_layout = new QHBoxLayout{first_widget};
//    first_layout->addWidget(first_widget);
//
//    QGridLayout* grid_layout = new QGridLayout{};
//    this->admin = new QPushButton("Admin mode");
//    this->user = new QPushButton("User mode");
//
//
//    grid_layout->addWidget(admin, 0, 0);
//    grid_layout->addWidget(user, 1, 0);
//
//
//    QWidget* buttons_widget = new QWidget{};
//    buttons_widget->setLayout(grid_layout);
//    first_layout->addWidget(buttons_widget);
//    first_dialog_window->addWidget(first_widget);
//
//
//   connect(admin,&QPushButton:: clicked, this, [this](){
//       this->main_window();
//
//
//   });
//
//}
//
//QWidget* GUI::admin_window(){
//    this->setWindowTitle("Master C++");
//    QWidget* admin_widget=new QWidget();
//
//
//}
//
//void GUI::main_window()
//{
//
//
//    QVBoxLayout* main = new QVBoxLayout{ this};
//
//
//
//    QWidget* up_widget = new QWidget{};
//    up_widget->setStyleSheet("background-color:lightgray;");
//    QHBoxLayout* upside_layout = new QHBoxLayout{up_widget };
//    upside_layout->addWidget(new QLabel{"Tutorials" });
//
//    this->list_of_tutorials_widget = new QListWidget{};
//    this->list_of_tutorials_widget->setSelectionMode(QAbstractItemView::SingleSelection);
//    upside_layout->addWidget(list_of_tutorials_widget);
//
//
//    QWidget* new_tutorial_widget = new QWidget{};
//    QFormLayout* form_layout = new QFormLayout{new_tutorial_widget };
//
//    this->title = new QLineEdit{};
//    QLabel* title_label = new QLabel{ "&Title:" };
//    title_label->setBuddy(title);
//    form_layout->addRow(title_label, title);
//
//    this->presenter = new QLineEdit{};
//    QLabel* presenter_label = new QLabel{ "&Presenter:" };
//    presenter_label->setBuddy(presenter);
//    form_layout->addRow(presenter_label, presenter);
//
//    this->likes = new QLineEdit{};
//    QLabel* likes_label = new QLabel{  "&Likes:"};
//    likes_label->setBuddy(likes);
//    form_layout->addRow(likes_label, likes);
//
//
//    this->link = new QLineEdit{};
//    QLabel* link_label = new QLabel{ "&Link:" };
//    link_label->setBuddy(link);
//    form_layout->addRow(link_label, link);
//
//
//    this->duration = new QLineEdit{};
//    QLabel* duration_label = new QLabel{ "&Duration:" };
//    duration_label->setBuddy(duration);
//    form_layout->addRow(duration_label, duration);
//
//    upside_layout->addWidget(new_tutorial_widget);
//
//
//    QGridLayout* grid_layout = new QGridLayout{};
//    this->addButton = new QPushButton("Add a tutorial");
//    this->deleteButton = new QPushButton("Delete a tutorial");
//    this->updateButton=new QPushButton("Update a tutorial");
//
//    grid_layout->addWidget(addButton, 0, 0);
//    grid_layout->addWidget(deleteButton, 1, 0);
//    grid_layout->addWidget(updateButton, 2, 0);
//
//    QWidget* buttons_widget = new QWidget{};
//    buttons_widget->setLayout(grid_layout);
//    upside_layout->addWidget(buttons_widget);
//
//
//    QWidget* middle_widget = new QWidget{};
//    QVBoxLayout* middle_layout = new QVBoxLayout{middle_widget };
//    this->add_to_watchlist_button = new QPushButton{"add to watchlist" };
//    middle_layout->addWidget(add_to_watchlist_button);
//
//
//    QWidget* down_widget = new QWidget{};
//    down_widget->setStyleSheet("background-color:lightgray;");
//    QHBoxLayout* downside_layout = new QHBoxLayout{down_widget};
//
//    this->watchList = new QListWidget{};
//
//    QWidget* watchlist_buttons = new QWidget{};
//    QHBoxLayout* watchlist_buttons_layout = new QHBoxLayout{watchlist_buttons};
//    this->nextButton=new QPushButton{"&Next tutorial" };
//    this->playButton=new QPushButton{"&Play tutorial" };
//    this->removeButton=new QPushButton{"&Remove tutorial from watchlist" };
//
//    watchlist_buttons_layout->addWidget(playButton);
//    watchlist_buttons_layout->addWidget(nextButton);
//    watchlist_buttons_layout->addWidget(removeButton);
//
//    downside_layout->addWidget(new QLabel{"Watchlist" });
//    downside_layout->addWidget(watchList);
//    downside_layout->addWidget(watchlist_buttons);
//
//
//    main->addWidget(up_widget);
//    main->addWidget(middle_widget);
//    main->addWidget(down_widget);
//    this->connect_signals_slots();

//}
//
//
//
//void GUI::add_list_of_tutorials(){
//
//    if(this->list_of_tutorials_widget->count()>0)
//        this->list_of_tutorials_widget->clear();
//
//    int i=0;
//    for(auto tutorial:this->list_tutorials){
//        QString t = QString::fromStdString(tutorial.to_string());
//        QListWidgetItem *listItemWidget = new QListWidgetItem(t);
//        this->list_of_tutorials_widget->insertItem(i,listItemWidget);
//        i++;
//    }
//    if(this->list_tutorials.size()>0)
//        this->list_of_tutorials_widget->setCurrentRow(0);
//}
//
//void GUI::add_new_tutorial(){
//    string new_title=title->text().toStdString();
//    string new_presenter=presenter->text().toStdString();
//    string new_link=link->text().toStdString();
//    string new_duration=duration->text().toStdString();
//    int new_likes=stoi(likes->text().toStdString());
//    string tutorial=new_title+','+new_presenter+','+new_duration+','+std::to_string(new_likes)+','+new_link;
//    std::stringstream stream{tutorial};
//
//    try{
//        Tutorial t;
//        stream>>t;
//        this->service.add_service(t);
//        list_tutorials=this->service.get_repo().get_all();
//        this->add_list_of_tutorials();
//    }
//    catch (Exception_Class& ex)
//    {
//        QMessageBox messageBox;
//        messageBox.critical(0,"Error",QString::fromStdString("Invalid"));
//    }
//
//
//}
//
//int GUI::get_selected_tutorial_index(){
//
//    if (list_of_tutorials_widget->count() == 0)
//        return -1;
//    QModelIndexList indexList = this->list_of_tutorials_widget->selectionModel()->selectedIndexes();
//    if (indexList.size() == 0)
//    {
//        presenter->clear();
//        title->clear();
//        likes->clear();
//        duration->clear();
//        link->clear();
//        return -1;
//    }
//    int index = indexList.at(0).row();
//    return index;
//}
////
////void GUI::add_watchlist(){
////    if (watchList->count() == 0)
////        watchList->clear();
////
////    for (auto t : *(this->service.get_watchlist()->get_all()))
////    {
////        QString itemInList = QString::fromStdString(t.get_title() + " - " + t.get_presenter());
////        this->watchList->addItem(itemInList);
////    }
////}
//
//void GUI::connect_signals_slots()
//{
//
//    QObject::connect(list_of_tutorials_widget,SIGNAL(itemSelectionChanged()),this,SLOT(listItemChanged()));
//    QObject::connect(this->addButton,SIGNAL(clicked()),this,SLOT(add_new_tutorial()));
//}
