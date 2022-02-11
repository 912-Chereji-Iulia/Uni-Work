//
// Created by Iulia on 16.04.2021.
//

#ifndef A67_912_CHEREJI_IULIA_CSV_H
#define A67_912_CHEREJI_IULIA_CSV_H


#include "File_Repo.h"

class CSV : public File_Repo{
protected:
    void save() override;
public:
     CSV(const string &file_name );
    ~CSV();
    void open() override;
};


#endif //A67_912_CHEREJI_IULIA_CSV_H
