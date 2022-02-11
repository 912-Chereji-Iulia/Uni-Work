//
// Created by Iulia on 17.04.2021.
//

#include "HTML.h"
#include "../validators/Exception_Class.h"
#include <windows.h>
#include <shellapi.h>
#include <fstream>

void HTML::save() {
    ofstream out(file_name);
    out << "<!DOCTYPE html>" << "\n";
    out << "<html>" << "\n";

    out << "<head>" << "\n";
    out << "<title>Watch List</title>" << "\n";
    out << "</head>" << "\n";

    out << "<body>" << "\n";

    out << "<table border=\"1\">" << "\n";

    out << "<tr>" << "\n";
    out << "<td>Title</td>" << "\n";
    out << "<td>Presenter</td>" << "\n";
    out << "<td>Duration</td>" << "\n";
    out << "<td>Nr likes</td>" << "\n";
    out << "<td>Link</td>" << "\n";
    out << "</tr>" << "\n";

    for (const auto& i : *this->get_all())
    {
        out << "<tr>" << "\n";

        out << "<td>" << i.get_title() << "</td>" << "\n";
        out << "<td>" << i.get_presenter() << "</td>" << "\n";
        out << "<td>" << i.get_duration() << "</td>" << "\n";
        out << "<td>" << i.get_nr_likes() << "</td>" << "\n";
        out << "<td><a href =" << i.get_link() << ">Link</a></td>";

        out << "</tr>"<<"\n" ;
    }

    out << "</table>" << "\n";

    out << "</body>" << "\n";

    out << "</html>"<< "\n" ;
    out.close();

}

void HTML::open() {

    ShellExecuteA(NULL, NULL,"chrome.exe", "C:\\Users\\Iulia\\Desktop\\Info\\a67-912-Chereji-Iulia\\cmake-build-debug\\Testing\\watchlist.html", NULL, SW_SHOWNORMAL);

}

HTML::~HTML() {
 this->save();
}

HTML::HTML(const string &file_name) : File_Repo(file_name) {
    this->file_name=file_name;
}



