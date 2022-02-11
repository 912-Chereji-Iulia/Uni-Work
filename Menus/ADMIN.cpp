//
// Created by Iulia on 13.05.2021.
//

#include "ADMIN.h"
#include "GUI.h"
#include "TutorialModel.h"
#include <sstream>
#include <iostream>


ADMIN::ADMIN(GUI* gui, Service_Tutorial &service, QWidget *parent) {
    this->gui=gui;
    this->service=service;

    this->main_window();

    this->list_tutorials= this->service.get_repo().get_all();
    this->add_list_of_tutorials();

}


void ADMIN::main_window() {
    this->setWindowTitle("Master C++ - Admin mode");
    QVBoxLayout* main = new QVBoxLayout{ this};

    QWidget* up_widget = new QWidget{};
    up_widget->setStyleSheet("background-color:lightgray;");
    QVBoxLayout* upside_layout = new QVBoxLayout{up_widget };
    upside_layout->addWidget(new QLabel{"Tutorials" });

    this->list_of_tutorials_widget = new QListWidget{};
    upside_layout->addWidget(list_of_tutorials_widget);
    
    QWidget* new_tutorial_widget = new QWidget{};
    QFormLayout* add_layout = new QFormLayout{new_tutorial_widget };

    this->title = new QLineEdit{};
    QLabel* title_label = new QLabel{ "&Title:" };
    title_label->setBuddy(title);
    add_layout->addRow(title_label, title);

    this->presenter = new QLineEdit{};
    QLabel* presenter_label = new QLabel{ "&Presenter:" };
    presenter_label->setBuddy(presenter);
    add_layout->addRow(presenter_label, presenter);

    this->likes = new QLineEdit{};
    QLabel* likes_label = new QLabel{  "&Likes:"};
    likes_label->setBuddy(likes);
    add_layout->addRow(likes_label, likes);


    this->link = new QLineEdit{};
    QLabel* link_label = new QLabel{ "&Link:" };
    link_label->setBuddy(link);
    add_layout->addRow(link_label, link);


    this->duration = new QLineEdit{};
    QLabel* duration_label = new QLabel{ "&Duration:" };
    duration_label->setBuddy(duration);
    add_layout->addRow(duration_label, duration);

    upside_layout->addWidget(new_tutorial_widget);

    this->addButton = new QPushButton("Add the tutorial");
    add_layout->addWidget(addButton);
    //upside_layout->addWidget(addButton);


    QWidget* delete_layout_widget=new QWidget{};
    QFormLayout* delete_layout=new QFormLayout{delete_layout_widget};
    this->title_delete = new QLineEdit{};
    QLabel* title_label_delete = new QLabel{ "&Title of tutorial to be deleted:" };
    title_label_delete->setBuddy(title_delete);
    delete_layout->addRow(title_label_delete, title_delete);
    upside_layout->addWidget(delete_layout_widget);
    this->deleteButton = new QPushButton("Delete the tutorial");
    upside_layout->addWidget(deleteButton);

    QWidget* update_layout_widget= new QWidget{};
    QFormLayout* update_layout=new QFormLayout{update_layout_widget};
    this->title_update=new QLineEdit{};
    QLabel* title_label_update = new QLabel{ "&Title of tutorial to be updated:" };
    title_label_update->setBuddy(title_update);
    update_layout->addRow(title_label_update, title_update);

    this->new_title = new QLineEdit{};
    QLabel* new_title_label = new QLabel{ "&New Title:" };
    new_title_label->setBuddy(new_title);
    update_layout->addRow(new_title_label, new_title);

    this->new_presenter = new QLineEdit{};
    QLabel* new_presenter_label = new QLabel{ "&New Presenter:" };
    new_presenter_label->setBuddy(new_presenter);
    update_layout->addRow(new_presenter_label, new_presenter);

    this->new_likes = new QLineEdit{};
    QLabel* new_likes_label = new QLabel{  "&New Likes:"};
    new_likes_label->setBuddy(new_likes);
    update_layout->addRow(new_likes_label, new_likes);


    this->new_link = new QLineEdit{};
    QLabel* new_link_label = new QLabel{ "&New Link:" };
    new_link_label->setBuddy(new_link);
    update_layout->addRow(new_link_label, new_link);


    this->new_duration = new QLineEdit{};
    QLabel* new_duration_label = new QLabel{ "&New Duration:" };
    new_duration_label->setBuddy(new_duration);
    update_layout->addRow(new_duration_label, new_duration);

    upside_layout->addWidget(new_tutorial_widget);

    upside_layout->addWidget(update_layout_widget);
    this->updateButton=new QPushButton("Update the tutorial");
    upside_layout->addWidget(updateButton);

    main->addWidget(up_widget);
    this->connect_signals_slots();

}

void ADMIN::add_list_of_tutorials() {
    if(this->list_of_tutorials_widget->count()>0)
        this->list_of_tutorials_widget->clear();

    int i=0;
    for(auto tutorial:this->list_tutorials){
        QString t = QString::fromStdString(tutorial.to_string());
        QListWidgetItem *listItemWidget = new QListWidgetItem(t);
        this->list_of_tutorials_widget->insertItem(i,listItemWidget);
        i++;
    }
    if(this->list_tutorials.size()>0)
        this->list_of_tutorials_widget->setCurrentRow(0);

}

void ADMIN::connect_signals_slots() {

    QObject::connect(this->addButton,&QPushButton::clicked,this,&ADMIN::add_new_tutorial);
    QObject::connect(this->deleteButton,&QPushButton::clicked,this,&ADMIN::delete_tutorial);
    QObject::connect(this->updateButton,&QPushButton::clicked,this,&ADMIN::update_tutorial);


}

void ADMIN::add_new_tutorial() {

    Validator val;
    string add_title=title->text().toStdString();
    string add_presenter=presenter->text().toStdString();
    string add_link=link->text().toStdString();
    string add_duration=duration->text().toStdString();
    string add_lkes=likes->text().toStdString();
    try{
        val.valid_duration(add_duration);
        val.valid_int(add_lkes);
        val.valid_link(add_link);
        val.valid_presenter(add_presenter);
        val.valid_title(add_title);
        int add_likes=stoi(add_lkes);

        string tutorial=add_title+','+ add_presenter+','+add_duration+','+std::to_string(add_likes)+','+add_link;
        std::stringstream stream{tutorial};

        Tutorial t;
        stream>>t;
        this->service.add_service(t);
        list_tutorials=this->service.get_repo().get_all();
        this->add_list_of_tutorials();
        title->clear();
        presenter->clear();
        duration->clear();
        link->clear();
        likes->clear();

    }
    catch (Exception_Class& ex){
        QMessageBox mb;
        mb.critical(0,"Error","Invalid input data");
    }
}


void ADMIN::delete_tutorial()
{
    string title_to_be_deleted=title_delete->text().toStdString();
    //std::stringstream stream{title_to_be_deleted};
    try{
        //stream>>title_to_be_deleted;

        this->service.delete_service(title_to_be_deleted);
        list_tutorials=this->service.get_repo().get_all();
        this->add_list_of_tutorials();
    }
    catch (Exception_Class& ex){
        QMessageBox mb;
        mb.critical(0,"Error","This tutorial doesn't exist");
    }

    title_delete->clear();

}

void ADMIN::update_tutorial()
{
    string title_to_be_updated=title_update->text().toStdString();
//    std::stringstream stream{title_to_be_updated};
//
//    stream>>title_to_be_updated;


    Validator val;
    string update_title=new_title->text().toStdString();
    string update_presenter=new_presenter->text().toStdString();
    string update_link=new_link->text().toStdString();
    string update_duration=new_duration->text().toStdString();
    string update_lkes=new_likes->text().toStdString();
    try{
        val.valid_duration(update_duration);
        val.valid_int(update_lkes);
        val.valid_link(update_link);
        val.valid_presenter(update_presenter);
        val.valid_title(update_title);
        int update_likes=stoi(update_lkes);

        string tutorial=update_title+','+update_presenter+','+update_duration+','+std::to_string(update_likes)+','+update_link;
        std::stringstream stream1{tutorial};


        Tutorial t;
        stream1>>t;
        this->service.update_service(title_to_be_updated,t);
        list_tutorials=this->service.get_repo().get_all();
        this->add_list_of_tutorials();
        title_update->clear();
        new_title->clear();
        new_presenter->clear();
        new_duration->clear();
        new_link->clear();
        new_likes->clear();


    }
    catch (Exception_Class& ex){
        QMessageBox mb;
        mb.critical(0,"Error","Invalid input data");
    }

}

void ADMIN::closeEvent(QCloseEvent *event) {
    this->gui->show();
    this->close();
}