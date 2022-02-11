//
// Created by Iulia on 05.03.2021.
//

#pragma once

#define cap 100
typedef void* TElement;
typedef void(*DestroyElementFunction)(void*);

typedef struct
{
    TElement* elems;
    int length;
    int capacity;
    DestroyElementFunction def;
} DynamicArray;

/// function that creates a dynamic array
/// \param capacity the capacity of the array
/// \param def The function that deals with deallocating the elements of the array
/// \return the dynamic array created
DynamicArray* createDynamicArray(int capacity, DestroyElementFunction def);

/// function that destroys the array
/// \param arr
void destroy(DynamicArray* arr);

/// function that resizes the dynamic array
/// \param arr
/// \return
int resize(DynamicArray* arr);

/// function that adds an element to the dynamic array
/// \param arr the array
/// \param t the element to be added
void add(DynamicArray* arr, TElement t);

/// function that deletes an element from the dynamic array
/// \param arr the array
/// \param p the element to be deleted
void delete(DynamicArray* arr, int p);

/// function that returns an element from a given position
/// \param arr the array
/// \param position the position of the elem
/// \return the element on the given position
TElement get_elem(DynamicArray* arr, int position);

/// function that return the length of the array
/// \param arr the array
/// \return its length
int get_arr_length(DynamicArray* arr);