//
// Created by Iulia on 05.03.2021.
//

#include "Array.h"
#include <stdlib.h>
#include <stdio.h>
#define cap 100

DynamicArray* createDynamicArray(int capacity, DestroyElementFunction def)
{
    DynamicArray* dyn_arr = (DynamicArray*)malloc(sizeof(DynamicArray));

    if (dyn_arr == NULL)
        return NULL;

    dyn_arr->capacity = capacity;
    dyn_arr->length = 0;
    dyn_arr->def = def;

    dyn_arr->elems = (TElement*)malloc(capacity * sizeof(TElement));


    return dyn_arr;
}

void destroy(DynamicArray* arr) {
    if (arr == NULL)
        return;
    for (int i = 0; i < arr->length; i++)
        arr->def(arr->elems[i]);
    free(arr->elems);
    arr->elems = NULL;
    free(arr);

}

int resize(DynamicArray* arr)
{   int i;
    if (arr == NULL)
        return 0;
    arr->capacity = arr->capacity*2;
    TElement* copy =(TElement*)malloc(arr->capacity*sizeof(TElement));
    if (copy == NULL)
        return -1;
    for (i=0;i<arr->length;i++)
        copy[i]=arr->elems[i];
    free(arr->elems);
    arr->elems =copy;
    return 0;
}

void add(DynamicArray* arr, TElement t)
{

    if (arr->length == arr->capacity)
        resize(arr);
    arr->elems[arr->length++] = t;

}

void delete(DynamicArray* arr, int p)
{

    if (p<0 || p>=arr->length)
        return;
    arr->def(get_elem(arr, p));
    for(int i=p;i<arr->length;i++)
        arr->elems[i]=arr->elems[i+1];
    arr->length --;
}

TElement get_elem(DynamicArray* arr, int position)
{
    return arr->elems[position];
}

int get_arr_length(DynamicArray* arr)
{
    return arr->length;
}