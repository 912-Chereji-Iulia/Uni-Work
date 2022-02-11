//
// Created by Iulia on 13.03.2021.
//
#include "Operations-List.h"
#include <stdlib.h>
#include <string.h>

Op* create_operation(Country* c, char* op_name)
{
    Op* op=(Op*)malloc(sizeof (Op));
    op->country=copy_country(c);

    op->op_name = (char*)malloc(sizeof(char) * (strlen(op_name) + 1));
    strcpy(op->op_name, op_name);

    return op;
}

Country* get_country(Op* op)
{
    return op->country;
}

char* get_op_name(Op* op)
{
    return op->op_name;
}

void destroy_op(Op* op)
{
    destroy_country(op->country);
    free(op->op_name);
    free(op);
}

Op* copy_operation(Op* op)
{
    if(op==NULL)
        return NULL;
    Op* new=create_operation(op->country,op->op_name);
    return new;
}

Op_list* create_list()
{
    Op_list* list=(Op_list*)malloc(sizeof(Op_list));
    list->length=0;
    return list;
}

void destroy_list(Op_list * list)
{
    int i;
    for(i=0;i<list->length;i++)
        destroy_op(list->operations[i]);
    free(list);
}

void add_op(Op_list* list, Op* o)
{
    Op* new=copy_operation(o);

    list->operations[list->length++]=new;

}

Op* remove_op(Op_list* list)
{
    if(list_empty(list))
        return NULL;
    list->length --;
    return list->operations[list->length];

}

int list_empty(Op_list* list)
{
    if(list->length==0)
        return 1;
    return 0;
}

