//
// Created by Iulia on 17.05.2021.
//

#ifndef A89_912_CHEREJI_IULIA_TUTORIALMODEL_H
#define A89_912_CHEREJI_IULIA_TUTORIALMODEL_H


#include <QAbstractListModel>

#include "../service/Service.h"

class TutorialModel : public QAbstractListModel{

private:
    Service_Tutorial service;
public:
    TutorialModel(Service_Tutorial service, QObject* parent=NULL);
     int row_count(const QModelIndex &parent = QModelIndex{}) const ;
    QVariant data(const QModelIndex &index, int role = Qt::DisplayRole) const override;


};


#endif //A89_912_CHEREJI_IULIA_TUTORIALMODEL_H
