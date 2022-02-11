//
// Created by Iulia on 17.04.2021.
//

#ifndef A67_912_CHEREJI_IULIA_HTML_H
#define A67_912_CHEREJI_IULIA_HTML_H


#include "File_Repo.h"

class HTML : public File_Repo {
protected:
    void save() override;

public:

    HTML(const string &file_name );
    ~HTML() ;
    void open() override;


};


#endif //A67_912_CHEREJI_IULIA_HTML_H
