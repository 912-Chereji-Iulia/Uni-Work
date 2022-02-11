#include "SMIterator.h"
#include "SortedMap.h"
#include <exception>


using namespace std;

SortedMap::SortedMap(Relation r) {
	this->rel=r;
    this->length=0;
    this->elements=new DLL;
	this->elements->head=NULL;
	this->elements->tail=NULL;
}//Theta(1)

TValue SortedMap::add(TKey k, TValue v) {
	TElem elem{k,v};

	DLLNode* new_node=new DLLNode; //create the node to be added
	new_node->next=NULL;
	new_node->prev=NULL;
	new_node->info=elem;

	if (this->elements->head==NULL) //list is empty
    {

	    this->elements->head=new_node;
        this->elements->tail=new_node;
        this->length = 1;
        return NULL_TVALUE;
    }
	if (this->rel(elem.first,(this->elements->head->info.first))){  //add at the beginning
        if (this->elements->head->info.first==elem.first){
            //the element with that key already exists so we have to update the value
            TValue old_val=this->elements->head->info.second;
            this->elements->head->info.second=elem.second;
            delete new_node;
            return old_val; //return the old value of the key

        }
        //make the new node the head of the list
        new_node->next=this->elements->head;
        this->elements->head->prev=new_node;
        this->elements->head=new_node;
        this->length++;
        return NULL_TVALUE;

    }
	if (this->rel((this->elements->tail->info.first),elem.first)){  //add at the end
	    if (this->elements->tail->info.first==elem.first){
	        //the element with that key already exists so we have to update the value
	        TValue old_val=this->elements->tail->info.second;
            this->elements->tail->info.second=elem.second;
            delete new_node;
            return old_val;//return the old value of the key
        }

        //make the new node the tail of the list
        new_node->prev=this->elements->tail;
        this->elements->tail->next=new_node;
        this->elements->tail=new_node;
        this->length++;
        return NULL_TVALUE;

	}

	DLLNode* current=this->elements->head;
	while (this->rel((current->next->info).first,elem.first))
	{
	    current = current->next;
	}

	if(current->info.first==elem.first)// if it is equal to the key of the pair stored at current
	{
	    TValue old_val=current->info.second;
	    current->info.second=elem.second;
	    delete new_node;
	    return old_val;
	}
	DLLNode* next_node = current->next;
	if(next_node->info.first==elem.first)// if it is equal to the key of the pair stored at the next node of current
	{
	    TValue old_val=next_node->info.second;
	    next_node->info.second=elem.second;
	    delete new_node;
	    return old_val;
	}
    //  insert it after the current node
	new_node->next=current->next;
	new_node->prev=current;
	next_node->prev=new_node;
	current->next=new_node;
	this->length++;
	return NULL_TVALUE;



} // BC: Theta(1),when the key of the given pair is supposed to be on the first or last position,or when we update the value associated to the first or last pairs already in the map
// WC:Theta(nr_of_pairs),when we have to compare the key of the given pair with all the other keys of the map
// -> total O(nr_of_pairs)


TValue SortedMap::search(TKey k) const {
    if(this->length==0) //list is empty
        return NULL_TVALUE;

    if(this->elements->head->info.first==k) //the searched element is the info of the head
        return this->elements->head->info.second;

    if(this->elements->tail->info.first==k) //the searched element is the info of the tail
        return this->elements->tail->info.second;

	DLLNode* current= this->elements->head;
	while(current->next!=NULL && this->rel(current->next->info.first,k))
	    current=current->next;

	if(current->next==NULL)
        return NULL_TVALUE;

    if ((current->info).first == k) //the key can be equal to the key of the current node
        return (current->info).second;
    else if (((current->next)->info).first == k) //the key can be equal to the key of the next node of current node
        return ((current->next)->info).second;
    else
        return NULL_TVALUE; //the pair with the given key is not in the map

}
//BC-theta(1), when the searched element is on the first or last position
//WC-theta(nr_pairs), when we have to verify every node
//total=O(nr_pairs)

TValue SortedMap::remove(TKey k) {
    if(this->length==0) //list is empty
        return NULL_TVALUE;

    if(this->elements->head->info.first==k) //remove the head
    {
        DLLNode* old_head = this->elements->head;
        TValue old_value = (old_head->info).second;
        if (old_head == this->elements->tail)// List has only one element, so it becomes empty after removing
        {
            this->elements->head = NULL;
            this->elements->tail = NULL;
        }
        else
        {
            this->elements->head = old_head->next;
            this->elements->head->prev = NULL;
        }
        delete old_head;
        this->length--;
        return old_value;
    }

    if(this->elements->tail->info.first==k) //remove the tail
    {
        DLLNode* old_tail = this->elements->tail;
        TValue old_value = (old_tail->info).second;

        this->elements->tail = old_tail->prev;
        this->elements->tail->next = NULL;
        delete old_tail;
        this->length--;
        return old_value;
    }

	DLLNode* current=this->elements->head;
	while(current->next!=NULL &&  this->rel( (current->next)->info.first,k))
    {
	    current=current->next;
    }

	if(current->next==NULL)
        return NULL_TVALUE;

    if ((current->info).first == k)//the key can be equal to the key of the current node
    {
        TValue removedValue = (current->info).second;
        current->next->prev = current->prev;
        current->prev->next = current->next;
        delete current;
        this->length--;
        return removedValue;
    }

    else if (((current->next)->info).first == k)//the key can be equal to the key of next node of the current node
    {
        TValue removedValue = current->next->info.second;
        current->next = current->next->next;
        current->next->prev = current;
        delete current;
        this->length--;
        return removedValue;
    }
    else
        return NULL_TVALUE; //element to be deleted is not in the map

}//BC-theta(1), when the element to be deleted is on the first or last position
//WC-theta(nr_pairs), when we have to verify every node
//total=O(nr_pairs)

int SortedMap::size() const {
	return this->length;

}//BC = WC = total complexity = theta(1)

//keeps in the SortedMap only those pairs whose key respects the given condition
void SortedMap::filter(Condition cond)
{
    DLLNode* current=this->elements->head;
    while(current!=NULL)
    {
        if(! cond(current->info.first))
        {
            this->remove(current->info.first);
        }
        current=current->next;
    }
} //Theta(nr_of_pairs)

bool SortedMap::isEmpty() const {
	if (this->length==0)
	    return true;
	return false;
}//BC = WC = total complexity = theta(1)


SMIterator SortedMap::iterator() const {
	return SMIterator(*this);

}//BC = WC = total complexity = theta(1)




SortedMap::~SortedMap() {

    delete [] elements;
}//BC = WC = total complexity = theta(nr of pairs)

