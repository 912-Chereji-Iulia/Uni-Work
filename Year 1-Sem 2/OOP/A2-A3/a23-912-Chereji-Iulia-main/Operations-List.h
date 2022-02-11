//
// Created by Iulia on 13.03.2021.
//

#pragma once
#pragma once
#include "Country.h"

typedef struct {
    Country* country;
    char* op_name;
}Op;
/// function that creates an operation
/// \param c the country on which the op will be performed
/// \param op_name the name of the operation
/// \return the operation created
Op* create_operation(Country* c, char* op_name);

/// function that destroys an operation
/// \param op the operation to be destroyed
void destroy_op(Op* op);

/// function that copies an operation
/// \param op the operation to be copied
/// \return the copy of the operation
Op* copy_operation(Op* op);

///
/// \param op the operation
/// \return the country of the operation
Country* get_country(Op* op);

///
/// \param op the operation
/// \return the name of the operation
char* get_op_name(Op* op);

typedef struct {
    Op* operations[1000];
    int length;
}Op_list;

/// function that creates a list of operations
/// \return the created list
Op_list * create_list();

/// function that destroys a list of operations
/// \param list the list to be destroyed
void destroy_list(Op_list * list);

/// function that adds an operation to the list
/// \param list
/// \param o the new operation
void add_op(Op_list* list, Op* o);

/// function that removes an operation from the list
/// \param list
/// \return the operation removed
Op* remove_op(Op_list* list);

/// function that checks if the list is empty
/// \param list
/// \return 1 if it is or 0 otherwise
int list_empty(Op_list* list);

