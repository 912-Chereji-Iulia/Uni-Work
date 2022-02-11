//
// Created by Iulia on 17.05.2021.
//

#include "TutorialModel.h"

TutorialModel::TutorialModel(Service_Tutorial service, QObject *parent) {

    this->service=service;
}

int TutorialModel::row_count(const QModelIndex &parent) const {
    int nr=this->service.get_repo().get_all().size();
    return nr;
}

QVariant TutorialModel::data(const QModelIndex &index, int role) const {
    int row=index.row();
    std::vector<Tutorial> tutorials=this->service.get_repo().get_all();
    if(row==tutorials.size())
        return QVariant();
    Tutorial t=tutorials[row];
    string returned_str=t.get_title()+","+t.get_presenter()+","+t.get_duration()+","+to_string(t.get_nr_likes())+","+t.get_link();
    return QString::fromStdString(returned_str);


}
