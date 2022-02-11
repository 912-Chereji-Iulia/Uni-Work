#include "SMIterator.h"
#include "SortedMap.h"
#include <exception>
#include <cstdlib>
#include <limits>

using namespace std;

SortedMap::SortedMap(Relation r) {
	this->rel=r;
	this->length=0;
	this->elems=new HashTable;
	this->elems->T=new Node*[8];
	this->elems->cap=8;
	for(int i=0;i<this->elems->cap;i++)
        this->elems->T[i]= nullptr;

	this->elems->max_load_factor=0.7;


}//Theta(cap)

TValue SortedMap::add(TKey k, TValue v) {


//    if(this->length/(double )this->elems->cap>=this->elems->max_load_factor)
//        this->resize();
    //the new node
    Node* new_node=new Node;
    new_node->info.first=k;
    new_node->info.second=v;
    new_node->next= nullptr;

    // Obtain its position
    int pos=this->hash_function(k);


    Node* current=this->elems->T[pos];
    if(current== nullptr) // If the position is not occupied
    {
        this->elems->T[pos]=new_node;
        this->length++;
        return NULL_TVALUE;
    }
    if(this->rel(k,current->info.first))
    {
        // We need to insert the new node at the beginning of the linked list situated at the current position
        if (current->info.first==k)
        {
            TValue old_val=current->info.second;
            current->info.second=v;
            delete new_node;
            return old_val;
        }
        new_node->next=current;
        this->elems->T[pos]=new_node;
        this->length++;
        return NULL_TVALUE;
    }
    // The new element is larger than the element at the beginning of the linked list situated at the current position, so we need to find where to insert it;
    while(current->next!=nullptr && !this->rel(k,current->next->info.first))
        current=current->next;
    // If the relation does not allow equality
    if(current->info.first==k){
        TValue old_val=current->info.second;
        current->info.second=v;
        delete new_node;
        return old_val;
    }

    Node* next_node=current->next;
    if(next_node != NULL)
    {
        // If the relation does not allow equality
        if(next_node->info.first == k)
        {   TValue old_val=next_node->info.second;
            next_node->info.second=v;
            delete new_node;
            return old_val;

        }
    }
    new_node->next=next_node;
    current->next=new_node;
    this->length++;
    return NULL_TVALUE;

}// Best Case: Theta(1) if the map is empty
// Worst Case: Theta(length) if all the elements in the map and the one to be added have the same hash value
// Total Complexity: O(length)

TValue SortedMap::search(TKey k) const {
	if(this->length==0)
	    return NULL_TVALUE;

	int pos=this->hash_function(k);
	Node* current=this->elems->T[pos];
	if(current== nullptr)
        return NULL_TVALUE;
	if(current->info.first==k)
        return current->info.second;

	while(current->next!= nullptr && !this->rel(k,current->next->info.first))
	    current=current->next;

	//if the relation doesn't allow equality
	if(current->info.first==k)
	    return current->info.second;
	Node* next_node=current->next;
	if(next_node!= nullptr)
    {
        //if the relation doesn't allow equality
	    if(next_node->info.first==k)
            return next_node->info.second;
    }
    return NULL_TVALUE;

}// Best Case: Theta(1) if the searched element is on the first pos or the sorted map is empty
// Worst Case: Theta(length) if the searched element is not in the sorted map
// Total Complexity: O(length)

TValue SortedMap::remove(TKey k) {
    if(this->length==0)
        return NULL_TVALUE;

    int pos=this->hash_function(k);
    Node* current=this->elems->T[pos];
    if(current== nullptr)
        return NULL_TVALUE;
    if(current->info.first==k)
    {
        TValue old_val=current->info.second;
        this->elems->T[pos]=current->next;
        delete current;
        this->length--;
        return old_val;

    }
    Node* prev=this->elems->T[pos];
    while(current->next!= nullptr &&!this->rel(k,current->next->info.first))
    {
        prev=current;
        current=current->next;
    }
    //if the relation doesn't allow equality
	if(current->info.first==k)
    {  TValue old_val = current->info.second;
        prev->next = current->next;
        delete current;
        this->length--;
        return old_val;
    }
	Node* next_node=current->next;
	if(next_node!= nullptr)
    {
        //if the relation doesn't allow equality
	    if(next_node->info.first==k)
        {
            TValue old_val = next_node->info.second;
            current->next = next_node->next;
            delete next_node;
            this->length--;
            return old_val;
        }
    }
    return NULL_TVALUE;
}// Best Case: Theta(1) if the element to be deleted is on the first pos or the sorted map is empty
// Worst Case: Theta(length) if the element to be deleted is not in the sorted map
// Total Complexity: O(length)

int SortedMap::size() const {

	return this->length;

}//Theta(1)

bool SortedMap::isEmpty() const {
	if(this->length==0)
	    return true;
    return false;

}//Theta(1)

//returns the difference between the maximum and the minimum key (assume integer keys)
int SortedMap::getKeyRange() const{
    if(this->length==0)
        return -1;
    int minim=std::numeric_limits<int>::max();
    int maxim=std::numeric_limits<int>::min();
    for(int i=0;i<this->elems->cap;i++)
    {
        if(this->elems->T[i]!= nullptr){
            if(this->elems->T[i]->info.first<minim)
                minim=this->elems->T[i]->info.first;
        }

    }
    for(int i=0;i<this->elems->cap;i++)
    {
        Node* current=this->elems->T[i];
        while(current!= nullptr){
            if(current->info.first>maxim)
                maxim=current->info.first;
            current=current->next;
        }

    }
    return abs(maxim-minim);

}//Theta(cap+lenght)


SMIterator SortedMap::iterator() const {
	return SMIterator(*this);
}//Theta(1)

SortedMap::~SortedMap() {

	int i;
	for(i=0;i<this->elems->cap;i++)
    {
	    Node* current;
	    while(this->elems->T[i]!= nullptr)
        {
	        current=this->elems->T[i]->next;
	        delete this->elems->T[i];
            this->elems->T[i]=current;
        }
    }
	delete[] this->elems;

}// Best case: Theta(capacity) if the map is empty
// Worst case: Theta(capacity * length) if all the TElems are in one SLL
// Total complexity: O(capacity * length)



int SortedMap::hash_function(TKey k) const {

    return abs(k) % this->elems->cap;

}//Theta(1)



void SortedMap::resize()
{

    int new_cap = 2 * this->elems->cap,i;
    this->length=0;
    Node** new_elems = new Node * [new_cap];
    for (i = 0; i < new_cap; i++)
    {
        new_elems[i] = nullptr;
    }
    int old_cap = this->elems->cap;
    this->elems->cap = new_cap;
    Node** old_hash_table = this->elems->T;
    this->elems->T = new_elems;
    for (i = 0; i < old_cap; i++)
    {
        if (old_hash_table[i] != nullptr)
        {
            Node* old;
            Node* current = old_hash_table[i];
            while (current != NULL)
            {
                this->add(current->info.first, current->info.second);
                old = current;
                current = current->next;
                delete old;
            }
        }
    }
    delete[] old_hash_table;

}//BC - Theta(2*cap), if the map is empty
//WC - Theta(2*cap*length), if all the elements in the map and the one to be added have the same hash value
//Total complexity - O(2*cap*length)


//copy constructor
SortedMap::SortedMap(const SortedMap& m) {
    this->rel=m.rel;
    this->elems = new HashTable;
    this->elems->T = new Node * [m.elems->cap];
    this->elems->max_load_factor = m.elems->max_load_factor;
    this->length = m.length;
    this->elems->cap = m.elems->cap;

    for (int i = 0; i < m.elems->cap; i++)
    {
        this->elems->T[i] = new Node;
        Node* node_current_map = this->elems->T[i];
        Node* node_other_map = m.elems->T[i];
        if (node_other_map != nullptr)
        {
            node_current_map->info = node_other_map->info;
            while (node_other_map->next != nullptr)
            {
                Node* newNode = new Node;
                newNode->info = node_other_map->next->info;
                node_current_map->next = newNode;
                node_current_map = newNode;
                node_other_map = node_other_map->next;
            }
            node_current_map->next = nullptr;
        }
        else
            this->elems->T[i] = NULL;
    }



}//Theta(length + cap)