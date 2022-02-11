//
// Created by Iulia on 16.03.2021.
//

#pragma once
#include "Tutorial.h"

template <typename TElem>

class Dyn_Array
{
private:
    TElem* elements;
    int length;
    int capacity;

    ///function to resize the dynamic array
    void resize();
public:
    ///constructor
    Dyn_Array(int cap=100);

    //copy constr
    //Dyn_Array(const Dyn_Array &da);

    ///destructor
    ~Dyn_Array();

    /// function to add an element to the dynamic array
    /// \param elem the element to be added
    void add(TElem elem);

    /// function to remove an element from the array
    /// \param position - position of the element to be removed
    void remove(int position);

    /// function to update an element from the array
    /// \param elem the new element
    /// \param position- position of the element to be updated
    void update(const TElem &elem, int position);

    /// function to get the length of the dynamic array
    /// \return the length
    int get_length() const;

    /// function that gets an element from the array by its position
    /// \param position - the position of the element
    /// \return the element on the given position
    TElem get_by_pos_dyn_arr(int position);



    TElem* get_all() const;

};

template <typename TElem>
Dyn_Array<TElem>::Dyn_Array(int capacity)
{
    this-> length = 0;
    this-> capacity = capacity;
    this->elements= new TElem[capacity];

}

//template<typename TElem>
//Dyn_Array<TElem>::Dyn_Array(const Dyn_Array<TElem> &da) {
//    this->length = da.length;
//    this->capacity = da.capacity;
//    this->elements = new TElem[this->capacity];
//    for (int i = 0; i < this->length; i++)
//        this->elements[i] = da.elements[i];
//}

template <typename TElem>
Dyn_Array<TElem>::~Dyn_Array()
{
    delete[] this->elements;

}


template <typename TElem>
void Dyn_Array<TElem>::add(TElem elem)
{
    if (this->length == this->capacity)
        this->resize();
    this->elements[this->length++]=elem;

}

template <typename TElem>
void Dyn_Array<TElem>::remove(int position)
{
    int i;
    for(i=position; i< this->length; i++)
        this->elements[i]= this->elements[i+1];
    this->length--;
}

template <typename TElem>
void Dyn_Array<TElem>::update(const TElem &elem, int position)
{
    this->elements[position] = elem;
}

template <typename TElem>
void Dyn_Array<TElem>::resize()
{
    this->capacity = this->capacity*2;
    TElem* copy=new TElem[this->capacity];
    int i;
    for(i=0;i< this->length;i++)
        copy[i]= this->elements[i];
    delete[] this->elements;
    this->elements=copy;
}

template <typename TElem>
int Dyn_Array<TElem>::get_length() const
{
    return this->length;
}

template <typename TElem>
TElem Dyn_Array<TElem>::get_by_pos_dyn_arr(int position) {
    return this->elements[position];
}

template <typename TElem>
TElem* Dyn_Array<TElem>::get_all() const{
    return this->elements;
}

