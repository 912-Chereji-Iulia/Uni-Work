#include "Set.h"
#include "SetIterator.h"
#include <exception>
#include <iostream>

using namespace std;

Set::Set() {

    this->capacity = 1;
    this->length = 0;
    this->elements = new bool[1];
    this->min=0;
    elements[0]=false;
}
//Theta(1)

bool Set::add(TElem elem) {

    //Element is already in the Set, we return false
    if(this->search(elem)==true)
        return false;

    //if the dynamic array is empty, we modify the elem on position 0 to true and the min becomes it
    if (this->isEmpty())
    {
        this->min = elem;
        this->elements[0] = true;
    }
    else if (elem < this->min) //if the added nr is smaller than the minimum
    {

        int bigger_capacity = this->capacity + this->min - elem;
        bool* resized_array = new bool[bigger_capacity];
        int i;

        resized_array[0] = true; //the new minimum, which will be elem, is on the first position
        for (i = 1; i < bigger_capacity; i++)
        {
            resized_array[i] = false; //the rest of the elements of the array are initialised with false
        }

        for (i = 0; i < this->capacity; i++)
        {
            if (this->elements[i] == true)    //Copy the existing values from the original array
            {
                int new_position= i+ this->min - elem;
                resized_array[new_position] = true;
            }

        }
        this->min = elem; //update the new minimum
        delete[] elements; //clean
        this->elements = resized_array; //update the array
        this->capacity = bigger_capacity; //update the capacity

    }
    else if (elem>= this->capacity+ this->min) //if the nr is bigger than the maximum nr, which is this->capacity+ this->min
    {
        int bigger_capacity = elem-this->min +1;
        bool* resized_array = new bool[bigger_capacity];
        int i;


        for (i = 0; i < bigger_capacity; i++)
        {
            resized_array[i] = false; //the elements of the array are initialised with false
        }

        for (i = 0; i < this->capacity; i++)
        {
            if (this->elements[i] == true)    //Copy the existing values from the original array
            {
                resized_array[i] = true;
            }

        }
        resized_array[elem-this->min]= true; //set the new value
        delete[] elements; //clean
        this->elements = resized_array; //update the array
        this->capacity = bigger_capacity; //update the capacity


    }
    else
    {
        this->elements[elem - this->min] = true;
    }
    this->length++; //we increase the length of the array
    return true;

}//Best case is Theta(1),when  we already have that element in in or if the nr we want to add is between
//min and max
// Worst case is Theta(capacity), when we have to resize the array
// => total complexity:O(capacity)

bool Set::remove(TElem elem) {
    //The given element is not in the set or the dynamic array is empty
    if (search(elem)==false || this->isEmpty())
        return false;

    //We set the value to false for the deleted element
    this->elements[elem - this->min] = false;

    if(elem==this->min) //if the element we want to delete is actually the minimum from the set
    {
        int i=0, pos_new_min;

        //find the new position of the minimum element in the dynamic array
        while(i<this->capacity-1 && this->elements[i]!= true)
            i++;
        pos_new_min=i;

        //we resize the dynamic array
        int smaller_capacity =this->capacity-pos_new_min;
        bool* resized_array= new bool[smaller_capacity];
        //we copy the old values in the newly created dynamic array
        i=0;
        for(int j=pos_new_min;j<=this->capacity-1;j++)
            resized_array[i++]=this->elements[j];

        //update the new dynamic array
        delete[] elements;
        this->elements = resized_array;
        this->capacity = smaller_capacity;

        int new_minimum = this->min + pos_new_min;
        this->min = new_minimum; //we set the new minimum
    }
    else if (elem==this->capacity+this->min)  // if the element we want to delete is the maximum one
    {
        int i,pos_new_max=this->capacity-1;
        //find the new position of the maximum element in the dynamic array
        i=pos_new_max;
        while(i>0 && this->elements[i]!=true)
            i--;
        pos_new_max = i;

        //we resize the dynamic array
        int smaller_capacity = pos_new_max+1;
        bool* resized_array= new bool[smaller_capacity];
        //we copy the old values in the newly created dynamic array
        i=0;
        for(int j=0;j<=pos_new_max;j++)
            resized_array[i++]=this->elements[j];

        //update the dynamic array
        delete[] elements;
        this->elements = resized_array;
        this->capacity = smaller_capacity;

    }

    this->length--; // we decrease the nr of elements in the set

    if(this->isEmpty())
        this->min=0; //if, by removing elements, we get an empty set, we reset the minimum

    return true;

}//Best case is Theta(1),when the array is empty or we don't have that element in in
// Worst case is Theta(capacity), when we have to resize the array
// => total complexity:O(capacity)


bool Set::search(TElem elem) const {
    //The searched element is not in the set
    if (elem < this->min)
        return false;

    //The searched element(with position elem - this->min) has the false value in the dyn array
    if(this->elements[elem-this->min] == false)
        return false;

    //the position of the searched element is bigger than the capacity of the dynamic array
    if(elem-this->min >= this->capacity)
        return false;


    return true;


}
//The complexity is Theta(1)

void Set::Union(const Set& s){

    SetIterator iterate_s=s.iterator();
    while(iterate_s.valid())
    {
        this->add(iterate_s.getCurrent());
        iterate_s.next();
    }
}
//Best case is Theta(capacity of s)
//Worst case is Theta(capacity of s* capacity of current set)
//total complexity O(capacity of s* capacity of current set)

int Set::size() const {
    return this->length;
}//BC, WC, TC Theta(1)


bool Set::isEmpty() const {
	if(this->length == 0)
	    return true;
	return false;
}
//BC, WC, TC Theta(1)


//destructor
Set::~Set() {
	delete[] this->elements;
}
//BC, WC, TC, Theta(1)

SetIterator Set::iterator() const {
	return SetIterator(*this);
}//BC,WC,TC Theta(1)


