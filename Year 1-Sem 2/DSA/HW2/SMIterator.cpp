#include "SMIterator.h"
#include "SortedMap.h"
#include <exception>

using namespace std;

SMIterator::SMIterator( const SortedMap& m) : map(m){
    this->current_node=map.elements->head;

}//BC = WC = total complexity = theta(1)

void SMIterator::first(){

    this->current_node=map.elements->head;

}//BC = WC = total complexity = theta(1)


void SMIterator::next(){
	if (!this->valid())
	    throw exception();
	else
	    this->current_node=this->current_node->next;
}//BC = WC = total complexity = theta(1)

bool SMIterator::valid() const{
	if (this->current_node!=NULL)
        return true;
	return false;
}//BC = WC = total complexity = theta(1)

TElem SMIterator::getCurrent() const{
    if (!this->valid())
        throw exception();
    else
        return this->current_node->info;

}//BC = WC = total complexity = theta(1)

