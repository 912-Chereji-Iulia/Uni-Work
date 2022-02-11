//
// Created by Iulia on 16.04.2021.
//

#ifndef A67_912_CHEREJI_IULIA_FILE_REPO_H
#define A67_912_CHEREJI_IULIA_FILE_REPO_H


#include "Watchlist.h"

class File_Repo : public Watchlist{

protected:
    string file_name;

    void save() override =0;

public:
    explicit File_Repo(const string &type): Watchlist(), file_name(type) {}
    virtual ~File_Repo()=default;
    virtual void open()=0;



};


#endif //A67_912_CHEREJI_IULIA_FILE_REPO_H
