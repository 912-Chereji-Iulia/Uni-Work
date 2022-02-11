#include "SetIterator.h"
#include "Set.h"
#include <exception>

using namespace std;

SetIterator::SetIterator(const Set& m) : set(m)
{
	this->current = 0;

}//Theta(1)


void SetIterator::first() {
	this->current = 0;
}//Theta(1)


void SetIterator::next() {
	if(not this->valid())
    {
        throw exception();
    }
	else
    {
	    int pos=this->current + 1;
	    while((this->set).elements[pos]==false && pos<(this->set).capacity)
	        pos++;
	    this->current=pos;
    }

}//BC, when it s not valid or the next element is on the next position: Theta(1),
// WC, when we don't have a next element which is true: Theta(capacity)
// Total Complexity: O(capacity)


TElem SetIterator::getCurrent()
{
    if(not this->valid())
    {
        throw exception();
    }
    return (this->set).min+this->current;
}//Theta(1)


bool SetIterator::valid() const {
    if ( (this->current == (this->set).capacity) || ((this->set).length == 0) )
    {
        return false;
    }
    return true;
}//Theta(1)



