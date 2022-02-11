
////
//// Created by Iulia on 21.03.2021.
////

#include "Tests.h"
#include "Dyn-Array.h"
#include "Tutorial.h"
#include "../repo/Repo.h"
#include "../service/Service.h"
#include "../repo/Watchlist.h"

#include <cassert>
#include <iostream>



void Tests::test_tutorial() {
    Tutorial t1{"C++ Tutorial for beginners", "Mike", "03:20", 132, "https://www.youtube.com/watch?v=vLnPwxZdW4Y"};
    assert(t1.get_nr_likes()==132);
    assert(t1.get_duration()=="03:20");
    assert(t1.get_presenter()=="Mike");
    assert(t1.get_title()=="C++ Tutorial for beginners");
    assert(t1.get_link()=="https://www.youtube.com/watch?v=vLnPwxZdW4Y");

    t1.set_likes(134);
    assert(t1.get_nr_likes()==134);

    string repr=t1.to_string();
    string r=t1.to_string_without_link();

    //t1.play_in_browser();


}

void Tests::test_repo() {
    Tutorial_Repo repo{};
    Tutorial t1{"C++ Tutorial for beginners", "Mike", "03:20", 132, "https://www.youtube.com/watch?v=vLnPwxZdW4Y"};
    repo.add_tutorial(t1);
    Tutorial t2{"C++ Tutorial 2020", "Derek Banas", "03:20", 200, "https://www.youtube.com/watch?v=6y0bp-mnYU0"};
    repo.add_tutorial(t2);
    assert(repo.get_repo_length()==2);

    int neok1=repo.add_tutorial(t2);
    assert(neok1==-1);
//    assert(repo.find_pos_by_title("C++ Tutorial for beginners")==0);
//    assert(repo.find_pos_by_link("https://www.youtube.com/watch?v=vLnPwxZdW4Y")==0);
    repo.delete_tutorial("C++ Tutorial for beginners");
    assert(repo.get_by_pos_repo(0).get_title()==t2.get_title());
    Tutorial t3{"C++ Tutorial 2020/2021", "Derek Banas", "03:20", 2100, "https://www.youtube.com/watch?v=6y0bp-mnYU0"};
    int ok=repo.update_tutorial("C++ Tutorial 2020",t3);
    assert(ok==1);
    int neok2=repo.update_tutorial("abk",t3);
    assert(neok2==-1);
    int neok3=repo.delete_tutorial("adkb");
    assert(neok3==-1);



}

void Tests::test_watchlist(){
    Watchlist list{};
    assert(list.size_of_watchlist()==0);
    Tutorial t1{"C++ Tutorial for beginners", "Mike", "03:20", 132, "https://www.youtube.com/watch?v=vLnPwxZdW4Y"};
    list.add_to_watchlist(t1);
    //assert(list.find_by_link(t1.get_link())==0);
    assert(list.get(0).get_title()==t1.get_title());
    list.remove_from_watchlist(t1);
    assert(list.size_of_watchlist()==0);
    assert(list.get(0).get_title()==Tutorial{}.get_title());


}


void Tests::test_service() {

    Service_Tutorial service{};

    Watchlist list{};
    Tutorial t1{"C++ Tutorial for beginners", "Mike", "03:20", 132, "https://www.youtube.com/watch?v=vLnPwxZdW4Y"};
    service.add_service(t1.get_title(),t1.get_presenter(),t1.get_duration(),t1.get_nr_likes(),t1.get_link());
    service.add_to_watchlist(t1);
    assert(service.get_service_length()==1);
    assert(service.get_by_position(0).get_title()==t1.get_title());
    service.delete_from_watchlist(t1);
    Tutorial t2{"C++ Tutorial 2020", "Derek Banas", "03:20", 200, "https://www.youtube.com/watch?v=6y0bp-mnYU0"};
    service.add_service(t2.get_title(),t2.get_presenter(),t2.get_duration(),t2.get_nr_likes(),t2.get_link());
    service.delete_service("C++ Tutorial for beginners");
    assert(service.get_by_position(0).get_title()==t2.get_title());
    Tutorial t3{"C++ Tutorial 2021", "Derek Banas", "03:20", 2020, "https://www.youtube.com/watch?v=6y0bp-mnYU0"};
    int ok=service.update_service("C++ Tutorial 2020",t3);
    assert(ok==1);

    service.add_to_watchlist(t3);

//    Tutorial_Repo presenters=service.search_by_presenter("Mike");
//    assert(presenters.get_repo_length()==0);
//
//    Tutorial_Repo presenters1=service.search_by_presenter("Derek Banas");
//    //assert(presenters1.get_repo_length()==1);
//
//    Tutorial_Repo presenters2=service.search_by_presenter("");
//    //assert(presenters1.get_repo_length()==1);




}


void Tests::test_all() {

    test_tutorial();
    test_repo();
    test_service();
    test_watchlist();
}


