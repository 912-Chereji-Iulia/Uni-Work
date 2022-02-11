//
// Created by Iulia on 13.05.2021.
//

#include <sstream>
#include "USER.h"

USER::USER(GUI *gui, Service_Tutorial &service, QWidget *parent) {
    this->gui=gui;
    this->service=service;
    this->watchlist=this->service.get_watchlist()->get_all();
    this->main_window();
    this->connect_signals_slots();

}

void USER::main_window() {
    this->setWindowTitle("Master C++ - User mode");
    QVBoxLayout* main = new QVBoxLayout{ this};



    QWidget* down_widget = new QWidget{};
    down_widget->setStyleSheet("background-color:lightgray;");
    QHBoxLayout* downside_layout = new QHBoxLayout{down_widget};

    this->watchList = new QListWidget{};
    this->list_by_presenter=new QListWidget{};

    QWidget* search_widget= new QWidget{};
    QFormLayout* search_layout=new QFormLayout{search_widget};
    this->presenter=new QLineEdit{};
    QLabel* presenter_label = new QLabel{ "&Presenter to search by:" };
    presenter_label->setBuddy(presenter);
    search_layout->addRow(presenter_label, presenter);


    QWidget* watchlist_buttons = new QWidget{};
    QVBoxLayout* watchlist_buttons_layout = new QVBoxLayout{watchlist_buttons};
    this->filterButton=new QPushButton{"&Filter by presenter" };
    this->nextButton=new QPushButton{"&Next tutorial" };
    this->playButton=new QPushButton{"&Play tutorial" };
    this->add_to_watchlist_Button=new QPushButton{"&Add to watchlist" };
    this->removeButton=new QPushButton{"&Remove tutorial from watchlist" };
    this->openButton=new QPushButton{"&Open the watchlist in an app." };
    watchlist_buttons_layout->addWidget(search_widget);
    watchlist_buttons_layout->addWidget(filterButton);
    watchlist_buttons_layout->addWidget(add_to_watchlist_Button);
    watchlist_buttons_layout->addWidget(playButton);
    watchlist_buttons_layout->addWidget(nextButton);
    watchlist_buttons_layout->addWidget(removeButton);
    watchlist_buttons_layout->addWidget(openButton);

    downside_layout->addWidget(new QLabel{"List filtered by presenter" });
    downside_layout->addWidget(list_by_presenter);


    downside_layout->addWidget(watchlist_buttons);
    downside_layout->addWidget(watchList);
    downside_layout->addWidget(new QLabel{"Watchlist" });

    main->addWidget(down_widget);

}


void USER::display_by_presenter(){
    if(this->list_by_presenter->count()>0)
        this->list_by_presenter->clear();

    int i=0;
    for(auto tutorial:this->list_tutorials){
        QString t = QString::fromStdString(tutorial.to_string());
        QListWidgetItem *listItemWidget = new QListWidgetItem(t);
        this->list_by_presenter->insertItem(i,listItemWidget);
        i++;
    }
    if(this->list_tutorials.size()>0)
        this->list_by_presenter->setCurrentRow(0);

}

void USER::display_watchlist() {
    if(this->watchList->count()>0)
        this->watchList->clear();


    for(auto tutorial:*this->watchlist){
        QString t = QString::fromStdString(tutorial.to_string());
        this->watchList->addItem(t);

    }
    if(this->watchlist->size()>0)
        this->watchList->setCurrentRow(0);
}

void USER::filter_by_presenter() {

    string presenter_search=presenter->text().toStdString();
//    std::stringstream stream{presenter_search};
//
//    stream>>presenter_search;
    list_tutorials=this->service.get_repo().search_by_presenter(presenter_search);
    this->display_by_presenter();

    if(list_tutorials.size()==0){
        QMessageBox mb;
        mb.critical(0,"Error","No tutorials by this presenter");
    }
    presenter->clear();
}

int USER::get_selected_tutorial_index(){
    if(list_by_presenter->count()==0)
        return -1;
    QModelIndexList index_list=this->list_by_presenter->selectionModel()->selectedIndexes();
    int index=index_list.at(0).row();
    return index;

}

void USER::play_tutorial(){
    int index=this->get_selected_tutorial_index_watchlist();
    this->service.get_watchlist()->get(index).play_in_browser();


}
int USER::get_selected_tutorial_index_watchlist(){
    if(watchList->count()==0)
        return -1;

    QModelIndexList index_list=this->watchList->selectionModel()->selectedIndexes();
    if(index_list.size()==0)
    {
        return -1;
    }
    int index=index_list.at(0).row();
    return index;

}

void USER::add_to_watchlist() {

try{
    Tutorial t=list_tutorials[get_selected_tutorial_index()];
    this->service.get_watchlist()->add_to_watchlist(t);
    this->watchlist=this->service.get_watchlist()->get_all();
    this->display_watchlist();
}

catch (Exception_Class& ex){
        QMessageBox mb;
        mb.critical(0,"Error","Invalid input data");
    }
}

void USER::delete_from_watchlist(){
    try{
        Tutorial t=this->watchlist->at(get_selected_tutorial_index_watchlist());

        this->service.delete_from_watchlist(t);
        QMessageBox mb1;
        mb1.setText("Did you enjoy this tutorial?");
        mb1.setStandardButtons( QMessageBox::No);
        QPushButton *yes_button=mb1.addButton(QMessageBox::Yes);
        mb1.exec();
        if(mb1.clickedButton()==yes_button)
        {
            t.set_likes(t.get_nr_likes()+1);
            Tutorial new_tutorial=Tutorial{t.get_title(),t.get_presenter(),t.get_duration(),t.get_nr_likes(),t.get_link()};
            this->service.update_service(t.get_title(),new_tutorial);

        }


        watchlist=this->service.get_watchlist()->get_all();
        this->display_watchlist();
    }
    catch (Exception_Class& ex){
        QMessageBox mb;
        mb.critical(0,"Error","Invalid input data");
    }


}

void USER::next_tutorial_watchlist(){
    int index;
    if(this->get_selected_tutorial_index()!=this->list_tutorials.size()) {
         index = this->get_selected_tutorial_index() + 1;
        this->list_by_presenter->setCurrentRow(index);
    }
    QMessageBox mb1;
    mb1.setText("Do you want to add this tutorial to watchlist?");
    mb1.setStandardButtons( QMessageBox::No);
    QPushButton *yes_button=mb1.addButton(QMessageBox::Yes);
    mb1.exec();
    if(mb1.clickedButton()==yes_button)
    {
        Tutorial t= this->list_tutorials[index];
        this->service.get_watchlist()->add_to_watchlist(t);
        this->watchlist=this->service.get_watchlist()->get_all();
        this->display_watchlist();
    }

}

void USER::open_watchlist(){
   this->service.get_watchlist()->open();
}


void USER::connect_signals_slots() {

    QObject::connect(this->filterButton,&QPushButton::clicked,this,&USER::filter_by_presenter);
    QObject::connect(this->add_to_watchlist_Button,&QPushButton::clicked,this,&USER::add_to_watchlist);
    QObject::connect(this->removeButton,&QPushButton::clicked,this,&USER::delete_from_watchlist);
    QObject::connect(this->nextButton,&QPushButton::clicked,this,&USER::next_tutorial_watchlist);
    QObject::connect(this->playButton,&QPushButton::clicked,this,&USER::play_tutorial);
    QObject::connect(this->openButton,&QPushButton::clicked,this,&USER::open_watchlist);
}

void USER::closeEvent(QCloseEvent *event) {
    this->gui->show();
    this->close();
}

