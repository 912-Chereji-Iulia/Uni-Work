//
// Created by Iulia on 18.03.2021.
//
#include <iostream>
#include <QApplication>
#include "repo/CSV.h"
#include "repo/HTML.h"
#include "repo/Repo.h"
#include "service/Service.h"
#include "ui/UI.h"
#include "tests/Tests.h"
#include "repo/File_Repo.h"
#include "ui/GUI.h"
#include "Menus/GUI.h"

//int main()
//{
//
//    try{
//        Tutorial_Repo repo("Tutorials.txt");
//        File_Repo* watchlist= nullptr;
//        cout<<"What file_name of file do you want to use? 1.CSV  2.HTML"<<endl;
//        int type;
//        cin>>type;
//        if(type==1)
//        {
//            watchlist=new CSV("C:\\Users\\Iulia\\Desktop\\Info\\a67-912-Chereji-Iulia\\cmake-build-debug\\Testing\\watchlist.csv");
//        }
//        else if (type==2)
//        {
//            watchlist= new HTML("C:\\Users\\Iulia\\Desktop\\Info\\a67-912-Chereji-Iulia\\cmake-build-debug\\Testing\\watchlist.html");
//        }
//        else
//            cout<<"Bad command";
//        Service_Tutorial service(repo,watchlist);
//        UI ui{service};
//        ui.start_me();
//        delete watchlist;
//    }
//    catch(Exception_Class& exc){
//        cout << exc.get_exception() << endl;
//    }
//
//    return 0;
//}

int main(int argc, char *argv[])
{
    QApplication a(argc,argv);
//    Tutorial_Repo repo("t1.txt");
//    File_Repo* watchlist=new CSV("watchlist.csv");
//    Service_Tutorial service(repo,watchlist);
    GUI w{0};
    w.show();
    return a.exec();
}

