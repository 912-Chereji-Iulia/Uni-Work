"""
Functions that implement program features. They should call each other, or other functions from the domain
"""

from src.domain.entity import get_expense_amount, set_expense_amount, check_int, get_expense_apartment, \
    check_expense_type, get_expense_type, get_expenses_values, get_expenses_history, set_expenses_values
import copy


def find_expense(expenses_values, value, category):
    """
    Finds the expenses which have the specified category value
    Raises a ValueError if arguments have wrong types or the search category is invalid
    :param expenses_values: List of expenses
    :param value: Key to be searched: id (int) or expense type (string)
    :param category: Keyword: 'id' or 'type'
    :return: A list of elements with the required value or None
    """
    if category == 'id':
        # Error handling
        check_int(value)
        ap_id = int(value)

        # Find the result
        result = list(filter(lambda x: get_expense_apartment(x) == ap_id, expenses_values))
        return result if len(result) > 0 else None
    elif category == 'type':
        # Error handling
        expense_type = value
        check_expense_type(value)

        # Find the result
        result = list(filter(lambda x: get_expense_type(x) == expense_type, expenses_values))
        return result if len(result) > 0 else None
    else:
        raise ValueError('The search category is invalid')


def get_expense_index(expenses_values, expense):
    """
    Finds the id of the first specified expense (search based on id and expense_type)
    :param expenses_values: List of expenses_values
    :param expense: Expense (dictionary)
    :return: Index of expense in expenses_values (int) or None
    """
    # result stores a list of pairs (index, expense) which correspond to the arguments
    for elem in expenses_values:
        if get_expense_apartment(elem) == get_expense_apartment(expense) and get_expense_type(elem) == get_expense_type(expense):
            return expenses_values.index(elem)


def add_expense(expenses, new_expense):
    """
    Adds a new expense to the expenses list
    :param expenses: Expenses (dict of expense values and history)
    :param new_expense: Expense (dictionary)
    :return: -
    """
    # We search to find an old expense with the same apartment and type, to sum it
    expenses_values = get_expenses_values(expenses)
    old_exp = get_expense_index(expenses_values, new_expense)

    # We add the list to the history
    expenses_history = get_expenses_history(expenses)
    values_copy = copy.deepcopy(expenses_values)
    expenses_history.append(values_copy)

    if old_exp is not None:
        old_amount = get_expense_amount(expenses_values[old_exp])
        set_expense_amount(expenses_values[old_exp], old_amount + get_expense_amount(new_expense))
    else:
        expenses_values.append(new_expense)


def remove_apartment_expenses(expenses, ap_id, f_call=False):
    """
    Removes all the expenses of apartment with specified id
    Raises ValueError if the arguments have wrong type
    :param expenses: Expenses (dict of expense values and history)
    :param ap_id: Id of apartment (int)
    :param f_call: If the function is called from another function or not
    :return: -
    """
    # Error handling
    check_int(ap_id)
    expenses_values = get_expenses_values(expenses)

    # Find every expense with specified apartment id and removes it
    apartment_expenses = find_expense(get_expenses_values(expenses), ap_id, 'id')
    if apartment_expenses is not None:
        if not f_call:
            # We add the list to the history
            history = get_expenses_history(expenses)
            history.append(copy.deepcopy(expenses_values))

        for expense in apartment_expenses:
            expenses_values.remove(expense)


def remove_type_expense(expenses, expense_type):
    """
    Removes all the apartment expenses with expense type specified
    Raises ValueError if arguments have wrong type
    :param expenses: Expenses (dict of expense values and history)
    :param expense_type: Expense type: water, heating, electricity, gas, other (string)
    :return: -
    """
    # Error handling
    check_expense_type(expense_type)
    expenses_values = get_expenses_values(expenses)

    # Find every expense with specified expense type and removes it
    apartment_expenses = find_expense(expenses_values, expense_type, 'type')
    if apartment_expenses is not None:

        # We add the list to the history
        history = get_expenses_history(expenses)
        history.append(copy.deepcopy(expenses_values))

        for expense in apartment_expenses:
            expenses_values.remove(expense)


def remove_apartments_expenses(expenses, ap_id1, ap_id2):
    """
    Removes all the apartment expenses of the apartments with id between id1 and id2
    Raises ValueError if arguments have wrong type or id1 > id2
    :param expenses: Expenses (dict of expense values and history)
    :param ap_id1: Start id (int)
    :param ap_id2: End id (int)
    :return: -
    """
    # Error handling
    check_int(ap_id1)
    check_int(ap_id2)
    ap_id1 = int(ap_id1)
    ap_id2 = int(ap_id2)

    # We add the list to the history
    history = get_expenses_history(expenses)
    history.append(copy.deepcopy(get_expenses_values(expenses)))

    if ap_id1 > ap_id2:
        raise ValueError('Second argument is smaller than the first')

    for ap_id in range(ap_id1, ap_id2 + 1):
        remove_apartment_expenses(expenses, ap_id, True)


def replace_expense(expenses, new_expense):
    """
    Replaces and old expense (with the same id and type as new_expense) amount
    Raises an error if it cannot find an expense to replace
    :param expenses: Expenses (dict of expense values and history)
    :param new_expense: Expense which will replace an old one (dictionary)
    :return: -
    """
    expenses_values = get_expenses_values(expenses)
    index = get_expense_index(expenses_values, new_expense)

    # Error handling
    if index is None:
        raise ValueError("Cannot find expense to replace")

    # We add the list to the history
    history = get_expenses_history(expenses)
    history.append(copy.deepcopy(expenses_values))

    set_expense_amount(expenses_values[index], get_expense_amount(new_expense))


def total_expenses_apartment(expenses_values, ap_id):
    """
    Returns the total expenses of an apartment by id ap_id
    Raises ValueError if arguments have wrong type
    :param expenses_values: List of expenses values
    :param ap_id: Id of apartment (positive integer)
    :return: Total expenses for the apartment ap_id (integer)
    """
    # Error handling
    check_int(ap_id)
    ap_id = int(ap_id)
    s=0
    for i in expenses_values:
        if get_expense_apartment(i) == ap_id:
            s = s+get_expense_amount(i)
    return s

def get_expenses_by_operator_and_value(expenses, operator, value):
    """
    Gets the list of apartments of which total expenses satisfy the operator and value (eg < 50)
    Raises ValueError if arguments have wrong type
    :param expenses: Expenses (dict of expense values and history)
    :param operator: Operator (<, =, >)
    :param value: Value to be compared (positive integer)
    :return: List of apartments which satisfy conditions
    """
    # Error handling
    check_int(value)
    value = int(value)
    if operator not in ['<', '=', '>']:
        raise ValueError('Operator is not valid')

    expenses_values = get_expenses_values(expenses)
    apartments = []
    if operator == '=':
        for x in expenses_values:
            if total_expenses_apartment(expenses_values, get_expense_apartment(x)) == value:
                if get_expense_apartment(x) not in apartments:
                    apartments.append(get_expense_apartment(x))

    elif operator == '<':
        for x in expenses_values:
            if total_expenses_apartment(expenses_values, get_expense_apartment(x)) < value:
                if get_expense_apartment(x) not in apartments:
                    apartments.append(get_expense_apartment(x))
    else:
        for x in expenses_values:
            if total_expenses_apartment(expenses_values, get_expense_apartment(x)) > value:
                if get_expense_apartment(x) not in apartments:
                     apartments.append(get_expense_apartment(x))
    return apartments


def get_apartment_expenses_list(expenses, ap_id):
    """
    Gets the expenses of an apartment
    Raises ValueError if arguments have wrong type
    :param expenses: Expenses (dict of expense values and history)
    :param ap_id: Id of apartment (positive integer)
    :return: List with expenses of apartment with id ap_id
    """
    # Error handling
    check_int(ap_id)
    ap_id = int(ap_id)

    expenses_values = get_expenses_values(expenses)
    l=[]
    for i in expenses_values:
        if get_expense_apartment(i) == ap_id:
            l.append(i)
    return l


def get_sum_of_expense_type(expenses, expense_type):
    """
    Returns the sum of all expenses of type specified
    Raises ValueError if type is invalid
    :param expenses: Expenses (dict of expense values and history)
    :param expense_type: Expense type: water, heating, electricity, gas, other (string)
    :return: Sum of all expenses of type specified (int)
    """
    # Error handling
    check_expense_type(expense_type)

    expenses_values = get_expenses_values(expenses)
    s = 0
    for i in expenses_values:
        if get_expense_type(i)==expense_type:
            s = s+get_expense_amount(i)
    return s


def get_max_apartment_expense(expenses, ap_id):
    """
    Returns the maximum expense of an apartment
    Raises ValueError if ap_id is invalid
    :param expenses: Expenses (dict of expense values and history)
    :param ap_id: Id of an apartment (integer)
    :return: Maximum expense of an apartment (integer or None)
    """
    # Error handling
    check_int(ap_id)
    ap_id = int(ap_id)

    # Gets the expense list of an apartment
    expenses_values = get_expenses_values(expenses)
    max=0
    for i in expenses_values:
        if get_expense_apartment(i)==ap_id:
            if get_expense_amount(i)>max:
                max=get_expense_amount(i)
    return max


def sort_apartments_by_expenses(expenses):
    """
    Returns a sorted list of apartments and their expenses
    :param expenses: Expenses (dict of expense values and history)
    :return: A sorted list of pairs (ap_id, total amount)
    """
    expense_values = get_expenses_values(expenses)
    apartment_and_exp_list=[]
    # Gets the list of tuples (ap_id, total_amount)
    for i in expense_values:
        apartment_and_exp_list.append((get_expense_apartment(i), total_expenses_apartment(expense_values, get_expense_apartment(i))))

    apartment_and_exp_list = list(dict.fromkeys(apartment_and_exp_list))
    # Sorting by the second parameter of the tuple
    apartment_and_exp_list.sort(key=lambda i: i[1])
    return apartment_and_exp_list


def sort_expense_types(expenses):
    """
    Returns a sorted list of expense types and their total value
    :param expenses: Expenses (dict of expense values and history)
    :return: A sorted list of pairs (expense_type, total amount)
    """
    # Gets the list of tuples (expense_type, total amount)
    expense_types = ['water', 'heating', 'electricity', 'gas', 'other']
    expense_types_list=[]
    for i in expense_types:
        if get_sum_of_expense_type(expenses,i):
            expense_types_list.append(((i, get_sum_of_expense_type(expenses, i))))

    # Sorts the list
    expense_types_list.sort(key=lambda x: x[1])
    return expense_types_list


def filter_by_expense_type(expenses, expense_type):
    """
    Removes from expenses any expense not having the expense type specified
    Raises ValueError if expense_type is invalid or if there is no expense with expense type specified
    :param expenses: Expenses (dict of expense values and history)
    :param expense_type: Expense type: water, heating, electricity, gas, other (string)
    """
    # Error handling
    check_expense_type(expense_type)
    expenses_values = get_expenses_values(expenses)
    new_expenses_list=[]
    for i in expenses_values:
        if get_expense_type(i)==expense_type:
            new_expenses_list.append(i)

    if not len(new_expenses_list):
        raise ValueError('Expense type to filter does not exist')

    # We check if it is necessary or not to modify something in the list
    if new_expenses_list != expenses_values:
        # We add the list to the history
        history = get_expenses_history(expenses)
        history.append(copy.deepcopy(expenses_values))
        set_expenses_values(expenses, new_expenses_list)


def filter_by_value(expenses, value):
    """
    Removes from expenses any expense having an amount bigger than value
    Raises a ValueError if the value is invalid or there is no expense with specified value
    :param expenses: Expenses (dict of expense values and history)
    :param value: Positive integer
    """
    # Error handling
    check_int(value)
    value = int(value)
    expenses_values = get_expenses_values(expenses)
    new_expenses_list=[]
    for i in expenses_values:
        if get_expense_amount(i)<value:
            new_expenses_list.append(i)

    if not len(new_expenses_list):
        raise ValueError('Expense values to filter do not exist')

    # We check if it is necessary or not to modify something in the list
    if new_expenses_list != expenses_values:
        # We add the list to the history
        history = get_expenses_history(expenses)
        history.append(copy.deepcopy(expenses_values))

        set_expenses_values(expenses, new_expenses_list)


def undo_expenses(expenses):
    """
    Undoes the last operation performed on the expense list
    Raises ValueError if there is no operation to undo
    :param expenses: Expenses (dict of expense values and history)
    """

    history = get_expenses_history(expenses)

    if len(history) == 0:
        raise ValueError('Cannot undo operation')

    new_value = history.pop()
    set_expenses_values(expenses, new_value)
