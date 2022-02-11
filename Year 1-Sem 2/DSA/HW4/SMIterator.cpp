#include "SMIterator.h"
#include "SortedMap.h"
#include <exception>

using namespace std;

SMIterator::SMIterator(const SortedMap& m) : map(m){
    this->first_position = 0;
    Node* current = this->map.elems->T[0];
    for (int i = 0; i < this->map.elems->cap; i++)
    {
        if (this->map.elems->T[i] != nullptr)
        {
            if (current == nullptr)
            {
                current = this->map.elems->T[i];
                this->first_position = i;
            }
            else
            {
                if (this->map.rel(this->map.elems->T[i]->info.first, current->info.first))
                {
                    current = this->map.elems->T[i];
                    this->first_position = i;
                }
            }

        }
    }
    this->current_position = first_position;

}//Theta(cap)

void SMIterator::first(){
    this->current_position = first_position;

}//Theta(1)

void SMIterator::next(){
    Node* current = this->copy.elems->T[this->current_position];
    if (current != nullptr)
    {
        Node* old_val = current;
        this->copy.elems->T[this->current_position] = current->next;
        current = current->next;
        delete old_val;
        for (int i = 0; i < this->copy.elems->cap; i++)
        {
            if (this->copy.elems->T[i] != nullptr)
            {
                if (current == nullptr)
                {
                    current = this->copy.elems->T[i];
                    this->current_position = i;
                }
                else
                {
                    if (this->map.rel(this->copy.elems->T[i]->info.first, current->info.first))
                    {
                        current = this->copy.elems->T[i];
                        this->current_position = i;
                    }
                }

            }
        }
        return;
    }
    throw exception();

}//Theta(cap)

bool SMIterator::valid() const{
    if (this->copy.elems->T[this->current_position] == nullptr)
        return false;
    return true;

}//Theta(1)

TElem SMIterator::getCurrent() const{
    if (!this->valid())
         throw exception();
    return this->copy.elems->T[this->current_position]->info;

}//Theta(1)


