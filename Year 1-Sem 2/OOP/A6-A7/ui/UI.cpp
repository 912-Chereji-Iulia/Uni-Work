//
// Created by Iulia on 18.03.2021.
//

#include "UI.h"
#include "../validators/Validator.h"
#include "../validators/Exception_Class.h"
#include <iostream>

#include <cstring>


using namespace std;



void UI::print_general_menu() {
    cout<<endl;
    cout<<"1. Administrator mode"<< endl;
    cout<<"2. User mode"<< endl;
    cout<<"0. Exit "<< endl;

}

void UI::print_admin_menu() {
    cout<<endl;
    cout<<"1. Add a tutorial"<<endl;
    cout<<"2. Delete a tutorial"<<endl;
    cout<<"3. Update a tutorial"<<endl;
    cout<<"4. Display all tutorials"<<endl;
    cout<<"0. Exit admin mode"<< endl;

}

void UI::print_user_menu() {
    cout<<endl;
    cout<<"1. See tutorials by presenter"<<endl;
    cout<<"2. See your watch list"<<endl;
    cout<<"3. Delete from watch list + rate the tutorial"<<endl;
    cout<<"4. Open watchlist in an app."<<endl;
    cout<<"0. Exit admin mode"<< endl;

}


void UI::add_tutorial_ui() {
    Validator val;

    cout<<"Enter the title of the tutorial: ";
    string title;
    getline(cin,title);



    cout<<"Enter the presenter of the tutorial: ";
    string presenter;
    getline(cin,presenter);


    cout<<"Enter the duration of the tutorial: ";
    string duration;
    getline(cin, duration);


    cout<<"Enter the number of likes: ";
    string lks;
    getline(cin, lks);


    cout<<"Enter the link of the tutorial: ";
    string link;
    getline(cin,link);

    try{
        val.valid_duration(duration);
        val.valid_int(lks);
        val.valid_link(link);
        val.valid_presenter(presenter);
        val.valid_title(title);

    }
    catch (Exception_Class& ex){
        cout << ex.get_exception() << endl;
        return;
    }
    int likes=stoi(lks);
    try{
        int ok=this->service.add_service(title,presenter,duration,likes,link);
    }
    catch (Exception_Class& ex){
        cout << ex.get_exception() << endl;
        return;
    }

    cout<<"Added"<<endl;

}

void UI:: delete_tutorial_ui()
{
    cout<<"Enter the title of the tutorial that you want to delete: ";
    string title;
    Validator val;
    getline(cin,title);
    try{
        val.valid_title(title);
    }
    catch (Exception_Class& ex){
        cout << ex.get_exception() << endl;
        return;

    }

    try{
        int ok=this->service.delete_service(title);
    }
    catch (Exception_Class& ex){
        cout << ex.get_exception() << endl;
        return;

    }

    cout<<"Deleted"<<endl;



}

void UI::update_tutorial_ui() {
    Validator val;
    cout<<"Enter the title of the tutorial that you want to update: ";
    string title;
    getline(cin,title);


    cout<<"Enter the new title of the tutorial: ";
    string new_title;
    getline(cin,new_title);


    cout<<"Enter the new presenter of the tutorial: ";
    string presenter;
    getline(cin,presenter);


    cout << "Enter the new duration (minutes and seconds): ";
    string duration;
    getline(cin, duration);


    cout<<"Enter the new number of likes: ";
    string lks;
    getline(cin,lks);

    cout<<"Enter the new link of the tutorial: ";
    string link;
    getline(cin,link);
    try{
        val.valid_duration(duration);
        val.valid_int(lks);
        val.valid_link(link);
        val.valid_presenter(presenter);
        val.valid_title(title);

    }
    catch (Exception_Class& ex){
        cout << ex.get_exception() << endl;
        return;
    }
    int likes=stoi(lks);



    try{
        Tutorial t{new_title,presenter,duration,likes,link};
        int ok=this->service.update_service(title,t);
    }
    catch (Exception_Class& ex){
        cout << ex.get_exception() << endl;
        return;
    }

    cout<<"Updated"<<endl;



}

void UI::display_all() {
    for (int i=0;i<this->service.get_service_length();i++)
        cout<<this->service.get_by_position(i).to_string()<<endl;

}

void UI::display_by_presenter()
{
    cout<<"Enter the presenter of the tutorial: ";
    string presenter;
    getline(cin,presenter);

    vector<Tutorial> repo=this->service.search_by_presenter(presenter);

    if(repo.size()==0)
        cout<<"There are no tutorials by this presenter"<<endl;
    else
    {
        int i=0;
        bool done=false;
        while(i<repo.size() || done==false)
        {
            cout <<repo[i].to_string_without_link()<<endl;
            repo[i].play_in_browser();
            this->add_to_watchlist(repo[i]);
            cout<<"Do you want to continue? 1.Yes 2.No "<<endl;
            int yes_or_no;
            cin>>yes_or_no;
            if(yes_or_no==2)
                break;

            i++;
            if(i==repo.size())
            {
                cout<<"Do you want to open from the beginning again? 1.Yes 2.No"<<endl;
                int ok;
                cin>>ok;
                if(ok==1)
                    i=0;
                else
                    done=true;
            }
        }
    }


}


void UI::add_to_watchlist(Tutorial t)
{
    cout<<"Do you want to add this to the watchlist? 1.Yes 2.No"<<endl;
    int yes_or_no;
    cin>>yes_or_no;

    if(yes_or_no==1)
    {
        try{
            if(this->service.get_watchlist()->find_by_link(t.get_link())==1)
            { this->service.add_to_watchlist(t);
                cout<<"Video added to playlist."<<endl;}
        }
        catch (Exception_Class& ex){
            cout << ex.get_exception() << endl;
            return;
        }

    }
    else
        cout<<"Video not added to playlist."<<endl;
}

void UI::delete_from_watchlist(){
    int i=0;
    while( i< this->service.get_watchlist()->size_of_watchlist())
    {
        Tutorial t=this->service.get_watchlist()->get(i);
        cout<<t.to_string_without_link()<<endl;
        cout<<"Do you want to delete this from the watchlist? 1.Yes 2.No"<<endl;
        int yes_or_no;
        cin>>yes_or_no;
        if(yes_or_no==1)
        {
            this->service.delete_from_watchlist(t);
            cout<<"Did you enjoy this tutorial? 1.Yes 2.No"<<endl;
            int like;
            cin>>like;
            if(like==1)
            {
                t.set_likes(t.get_nr_likes()+1);
                Tutorial new_tutorial=Tutorial{t.get_title(),t.get_presenter(),t.get_duration(),t.get_nr_likes(),t.get_link()};
                this->service.update_service(t.get_title(),new_tutorial);
                cout<<t.to_string()<<endl;
            }
            cout<<"Video deleted from playlist."<<endl;
        }
        else
        {
            cout<<"Video not deleted from playlist."<<endl;
            i++;
        }
    }

}



//void UI::start_entries()
//{
//    this->service.add_service("C++ Tutorial for beginners", "Mike", "03:20", 132, "https://www.youtube.com/watch?v=vLnPwxZdW4Y");
//    this->service.add_service("C++ Tutorial 2020", "Derek Banas", "03:20", 200, "https://www.youtube.com/watch?v=6y0bp-mnYU0");
//    this->service.add_service("C++ Programming, Lecture# 1", "Paul", "03:20", 100, "https://www.youtube.com/watch?v=NiqeMDMPFY8");
//    this->service.add_service("C++ Programming, Lecture # 2", "Paul", "03:20", 120, "https://www.youtube.com/watch?v=y4i3kXw3NWw");
//    this->service.add_service("C++ Programming Tutorial 1 - Intro to C++", "Caleb Curry", "03:20", 10000, "https://www.youtube.com/watch?v=OTroAxvRNbw");
//    this->service.add_service("C++ Programming | In One Video", "Mike Dane", "03:20", 1372, "https://www.youtube.com/watch?v=raZSmcariyU");
//    this->service.add_service("C++ Crash Course For Beginners", "Traversy Media", "03:20", 232, "https://www.youtube.com/watch?v=1v_4dL8l8pQ");
//    this->service.add_service("Dino game in C++", "Idli", "03:20", 13872, "https://www.youtube.com/watch?v=CxXDhKL7dX4");
//    this->service.add_service("C++ from Basic", "Extern Code", "03:20", 1342, "https://www.youtube.com/watch?v=mUQZ1qmKlLY");
//    this->service.add_service("Pointers", "The Chernos", "03:20", 132, "https://www.youtube.com/watch?v=DTxHyVn0ODg");
//}


void UI::start_me()
{
    bool done=false;
    //start_entries();
    this->service.load_repo();
    //this->service.start_watchlist();
    while(done==false)
    {
        UI::print_general_menu();

        cout<<"Choose a mode>> ";
        int cmd;
        cin>>cmd;
        if(cmd==0)
        { cout<<"Bye bye!";
            done= true;
        }
        else if (cmd==1)
        {
            bool done_admin=false;
            while(done_admin==false)
            {
                UI::print_admin_menu();

                cout<<"Enter a command>> ";
                int cmd_admin;
                cin>>cmd_admin;
                cin.ignore();
                if (cmd_admin==0)
                {
                    cout<<"Exiting admin mode!"<<endl;
                    done_admin=true;
                }
                else
                if(cmd_admin==1)
                    this->add_tutorial_ui();
                else if(cmd_admin==4)
                    this->display_all();
                else if(cmd_admin==2)
                    this->delete_tutorial_ui();
                else if (cmd_admin==3)
                    this->update_tutorial_ui();
                else
                    cout<<"Invalid command";
            }
        }
        else if(cmd==2)
        {
            bool done_user=false;
            while(done_user==false)
            {
                UI::print_user_menu();

                cout<<"Enter a command>> ";
                int cmd_user;
                cin>>cmd_user;
                cin.ignore();
                if (cmd_user==0)
                {
                    cout<<"Exiting user mode!"<<endl;
                    done_user=true;
                }
                else
                if(cmd_user==1)
                    this->display_by_presenter();
                else if (cmd_user==2)
                    this->display_watchlist();
                else if (cmd_user==3)
                    this->delete_from_watchlist();
                else if(cmd_user==4)
                    this->open_app();
                else
                    cout<<"Invalid command";



            }

        }
        else
        {
            cout<<"Invalid command!";
        }

    }
}

void UI::display_watchlist() {
    for(int i=0;i<this->service.get_watchlist()->size_of_watchlist();i++)
        cout<<this->service.get_watchlist()->get(i).to_string()<<endl;

}

UI::UI(Service_Tutorial &service) {
    this->service=service;
}

void UI::open_app() {
    this->service.open_app();

}

