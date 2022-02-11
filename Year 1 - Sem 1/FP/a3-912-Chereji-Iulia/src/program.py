
#
# Write the implementation for A3 in this file
#

#
# domain section is here (domain = numbers, transactions, expenses, etc.)
# getters / setters
# No print or input statements in this section
# Specification for all non-trivial functions (trivial usually means a one-liner)
def check_int(x):
    """
    Raises an error if x is not a positive integer
    :param x:
    :return:
    """
    try:
        x = int(str(x))
        if x <= 0:
            raise ValueError
    except ValueError:
        raise ValueError('Should be a positive integer!')


def check_type(x):
    """
    Raises an error if x is not an expense type ('water', 'heating', 'electricity', 'gas', 'other')
    :param x:
    :return:
    """
    try:
        if x not in ['water', 'heating', 'electricity', 'gas', 'other']:
            raise ValueError
    except ValueError:
        raise ValueError('Should be a valid expense type:(water, heating, electricity, gas, other)')


def create_apartment_expense( list ):
    """
    create an apartment expense with given parameteres
    :return: the created apartment expense
    """
    check_int(list[0])
    check_type(list[1])
    check_int(list[2])
    id= int(list[0])
    type= str(list[1])
    amount= int(list[2])
    return {'id': id, 'type': type, 'amount': amount}


def get_id(ap):
    return ap['id']


def get_amount(ap):
    return ap['amount']


def set_amount(ap,value):
    ap['amount']=value


def get_type(ap):
    return ap['type']


def to_str(ap):
    return 'Apartment ' + str(get_id(ap)) + ' type: ' + str(get_type(ap)) + ' amount: ' + str(get_amount(ap))


# Functionalities section (functions that implement required features)
# No print or input statements in this section
# Specification for all non-trivial functions (trivial usually means a one-liner)
# Each function does one thing only
# Functions communicate using input parameters and their return values

def add_expense(expense_list, expense):
    """
    Adds an expense to the list
    :param expense_list: list of expenses
    :param expense: the new expense
    :return:-
    We search to find an old expense with the same apartment and type, to sum it
    """
    old_expense = get_expense_index(expense_list, expense)
    if old_expense is None:
        expense_list.append(expense)
    else:
        old_amount = get_amount(expense_list[old_expense])
        set_amount(expense_list[old_expense], old_amount+get_amount(expense))


def get_list_apartment_expenses(expense_list, id):
    """
    gets the expenses of an apartment
    :param expense_list:
    :param id: id of apartment
    :return: list with expenses of ap with id id
    """
    try:
       check_int(id)
       id = int(id)
    except ValueError:
       raise ValueError("Apartment id should be an integer")
    ap_exp = []
    for i in expense_list:
       if get_id(i) == id:
           ap_exp.append(i)
    return ap_exp


def total_expenses_apartment(expense_list, id):
    """
    Returns the total expenses of an apartment by id
    :param expense_list:
    :param id:
    :return: the total number of expenses
    """
    try:
        check_int(id)
        id = int(id)
    except ValueError:
        raise ValueError("Apartment id should be an integer")
    total = 0
    for i in expense_list:
        if get_id(i) == id:
            total += get_amount(i)
    return total


def get_expense_list_operator(expense_list, operator, total):
    """
    Gets the list of apartments of which total expenses satisfy the operator and value (eg < 50)
    :param expense_list:
    :param operator: = > <
    :param total:
    :return: list of apartments which satisfy the condition
    """
    check_int(total)
    total = int(total)
    if operator not in ['=', '>', '<']:
        raise ValueError('Operator is not valid!')
    ap = []
    if operator == '=':
        for i in expense_list:
            if total_expenses_apartment(expense_list, get_id(i)) == total:
                if get_id(i) not in ap:
                    ap.append(get_id(i))
    elif operator == '<':
        for i in expense_list:
            if total_expenses_apartment(expense_list, get_id(i)) < total:
                if get_id(i) not in ap:
                    ap.append(get_id(i))
    else:
        for i in expense_list:
            if total_expenses_apartment(expense_list, get_id(i)) > total:
                if get_id(i) not in ap:
                    ap.append(get_id(i))
    return ap


def get_expense_index(expense_list, expense):
    """
    Finds the id of the first specified expense (search based on id and expense_type)
    :param expense_list:
    :param expense:
    :return:Index of expense in expense_list (int) or None
    """
    result = [(idx, entry) for idx, entry in enumerate(expense_list) if get_type(entry) == get_type(expense) and get_id(entry) == get_id(expense)]
    if result:
        return result[0][0]
    else:
        return None

def print_expenses(expense_list):
    for expense in expense_list:
        print(to_str(expense))

def find_expense(expense_list, key, category):
    """
    finds the expenses which have the specified category value
    :param expense_list:
    :param key: id or type
    :param category: 'id' or 'type'
    :return: A list of elements with the required value or None
    """
    if category== 'id':
        try:
            check_int(key)
            ap_id = int(key)
        except ValueError:
            raise ValueError("Apartment id to be found is not a positive integer")
        '''result=[]
        for i in expense_list:
            if get_id(i)==id:
                result.append(i)
        '''
        result = list(filter(lambda x: get_id(x) == ap_id, expense_list))
        if len(result) > 0:
            return result
        else:
            return None
    elif category == 'type':
        type=key
        check_type(key)
        '''result = []
        for i in expense_list:
            if get_type(i) == type:
                result.append(i)
        '''
        result = list(filter(lambda x: get_type(x) == type, expense_list))
        if len(result) > 0:
            return result
        else:
            return None
    else:
        return ValueError('The search category is invalid')




def remove_apartment_expenses(expense_list, id):
    """
    removes all the expenses of an apartment with a given id
    :param expense_list:
    :param id:
    :return:
    """
    try:
        check_int(id)
        id = int(id)
    except ValueError:
        raise ValueError("Apartment id to be removed should be an integer")
    ap_exp= find_expense(expense_list, id,'id')
    if ap_exp is not None:
        for i in ap_exp:
            expense_list.remove(i)


def remove_type_expense(expense_list, type):
    """
     Removes all the apartment expenses with expense type specified
    :param expense_list:
    :param type:
    :return:
    """
    check_type(type)
    ap_exp=find_expense(expense_list,type,'type')
    if ap_exp is not None :
        for i in ap_exp:
            expense_list.remove(i)


def remove_interval(expense_list, id1,id2):
    """
     Removes all the apartment expenses of the apartments with id between id1 and id2
    :param expense_list:
    :param id1:
    :param id2:
    :return:
    """
    try:
        check_int(id1)
        check_int(id2)
        id1=int(id1)
        id2=int(id2)
    except ValueError:
        raise ValueError
    for id in range(id1,id2+1):
        remove_apartment_expenses(expense_list,id)


def replace_expense(expense_list, new_expense):
    """
    Replaces and old expense (with the same id and type as new_expense) amount
    :param expense_list:
    :param new_expense:
    :return:
    """
    index= get_expense_index(expense_list, new_expense)
    if index is None:
        raise ValueError("Cannot find expense to replace")
    set_amount(expense_list[index],get_amount(new_expense))


def split_command(command):
    """
    Split command string into command word and parameters
    :param command: (command_word, command_params)
    :return:
    """
    command = command.strip()
    tokens = command.split(' ',1)
    command_word = tokens[0].strip().lower()
    if len(tokens)==2:
        command_params = tokens[1].strip().lower()
    else:
        command_params =''
    return command_word, command_params

# UI section
# (all functions that have input or print statements, or that CALL functions with print / input are  here).
# Ideally, this section should not contain any calculations relevant to program functionalities


def start_command_ui():
    expense_list = []
    test_init(expense_list)
    command_dict = {'add':add_command,'list':display_command_ui,'remove':remove_command_ui, 'replace':replace_command_ui}
    done = False
    while not done:
        command = input("command>>>")
        try:
            cmd_word, cmd_params = split_command(command)
            if cmd_word in command_dict:
                command_dict[cmd_word](expense_list,cmd_params)
            elif cmd_word == 'exit':
                print('Bye bye!')
                done=True
            else:
                print ('Invalid command!')
        except ValueError as ve:
            print(str(ve))

def add_command(expense_list,expense):
    """
     Adds new expenses to the entry
    :param expense_list:
    :param expense:
    :return:
    """
    tokens=expense.split(',')
    for token in tokens:
        token=token.strip()
        list=token.split( )
        if len(list) !=3 :
            raise ValueError("Invalid number of arguments")
        new_exp = create_apartment_expense(list)
        add_expense(expense_list, new_exp)


def display_command_ui(expenses, arguments):
    """
    Lists the expenses based on arguments
    :param expenses: List of expenses
    :param arguments: Arguments for the replace function
    :return: -
    """
    # Split arguments, if there are more than 1
    tokens = arguments.split(',')
    for token in tokens:
        token = token.strip().split()
        if not token:
            print_expenses(expenses)
        elif len(token) == 1:
            apartment_expenses = get_list_apartment_expenses(expenses, token[0])
            print_expenses(apartment_expenses)
        elif len(token) == 2:
            apartments = get_expense_list_operator(expenses, token[0], token[1])
            if len(apartments) == 0:
                print("There are no apartments with this property")
            else:
                print('Apartments are: ', *apartments)
        else:
            raise ValueError('Invalid number of arguments for list')

def remove_command_ui(expense_list, arguments):
    """
    Removes specified expenses from the entry list
    :param expense_list:
    :param arguments:
    :return:
    """
    tokens=arguments.split(', ')
    for token in tokens:
        token=token.strip().split()
        if not token[0] or len(token) > 3 :
            raise ValueError("Invalid number of arguments ")
        if len(token)==1:
            if token[0] in ['water', 'gas', 'heating','electricity','other']:
                remove_type_expense(expense_list,token[0])
            else:
                remove_apartment_expenses(expense_list, token[0])
        else:
            if token[1] != 'to':
                print("Invalid command")
            else:
                 remove_interval(expense_list,token[0], token[2])

def replace_command_ui(expense_list,arguments):
    """
    Replaces specified expense type in specified apartment
    :param expense_list:
    :param arguments:
    :return:
    """
    tokens = arguments.split(',')
    for token in tokens:
        token = token.strip().split()
        if 'with' not in token:
            raise ValueError("Invalid replace argument")
        token.remove('with')
        new_expense = create_apartment_expense(token)
        replace_expense(expense_list, new_expense)

# Test functions go here
#
# Test functions:
#   - no print / input
#   - great friends with assert

def test_init(test_ls):
    # use this function to add the 10 required items
    # use it to set up test data
    test_ls.clear()
    test_ls.append(create_apartment_expense(['1', 'gas', '20']))
    test_ls.append(create_apartment_expense(['2', 'water', '30']))
    test_ls.append(create_apartment_expense(['1', 'other', '10']))
    test_ls.append(create_apartment_expense(['3', 'electricity', '200']))
    test_ls.append(create_apartment_expense(['2', 'gas', '250']))
    test_ls.append(create_apartment_expense(['3', 'heating', '280']))
    test_ls.append(create_apartment_expense(['4', 'heating', '120']))
    test_ls.append(create_apartment_expense(['7', 'other', '520']))
    test_ls.append(create_apartment_expense(['2', 'electricity', '10']))
    test_ls.append(create_apartment_expense(['1', 'heating', '2']))

def test_create_expense():
    create_apartment_expense([1, 'gas', 10])
    create_apartment_expense(['1', 'gas', 10])
    try:
        create_apartment_expense(['a', 'gas', '10'])
        assert False
    except ValueError:
        assert True

    try:
        create_apartment_expense(['1', 'air', '10'])
        assert False
    except ValueError:
        assert True

    try:
        create_apartment_expense(['1', 'gas', '-10'])
        assert False
    except ValueError:
        assert True

    try:
        create_apartment_expense(['1', 'gas', 10.747])
        assert False
    except ValueError:
        assert True

def test_add():
    #test adding to the list
    test_ls=[]
    aux=create_apartment_expense(['1','gas','20'])
    add_expense(test_ls,aux)
    # checks adding a normal elem
    assert len(test_ls)==1

    set_amount(aux,30)
    add_expense(test_ls,aux)

    #checks adding a new amount to an old elem
    assert len(test_ls)==1

    aux = create_apartment_expense(['2', 'water', '30'])
    add_expense(test_ls, aux)

    assert len(test_ls) == 2


def test_find_expense():
    # Checks the finding functions
    test_ls = []
    test_init(test_ls)

    aux = find_expense(test_ls, 'gas', 'type')
    assert len(aux) == 2

    aux = find_expense(test_ls, '1', 'id')
    assert len(aux) == 3

    aux = find_expense(test_ls, '100', 'id')
    assert aux is None

    expense = test_ls[0]
    aux = get_expense_index(test_ls, expense)
    assert aux == 0

def test_remove():
    # Checks the remove functions
    test_ls = []

    test_init(test_ls)
    remove_type_expense(test_ls, 'water')
    assert len(test_ls) == 9

    test_init(test_ls)
    remove_apartment_expenses(test_ls, 2)
    assert len(test_ls) == 7

    test_init(test_ls)
    remove_interval(test_ls, 1, 10)
    assert len(test_ls) == 0

    try:
        remove_type_expense(test_ls, 'air')
        assert False
    except ValueError:
        assert True

    try:
        remove_apartment_expenses(test_ls, 147.7)
        assert False
    except ValueError:
        assert True


def test_replace():
    # Tests the replace function
    test_ls = []
    test_init(test_ls)

    aux = create_apartment_expense(['1', 'gas', '30'])
    replace_expense(test_ls, aux)

    assert get_amount(aux) == 30

    try:
        aux = create_apartment_expense([100, 'water', 10])
        replace_expense(test_ls, aux)
        assert False
    except ValueError:
        assert True


def test_total_expenses():
    # Tests the total expenses function
    test_ls = []
    test_init(test_ls)

    aux = create_apartment_expense([11, 'gas', 112])

    assert total_expenses_apartment(test_ls, 2) == 290

    add_expense(test_ls, aux)

    assert total_expenses_apartment(test_ls, 11) == 112


def test_list_func():
    # Tests the list functions
    test_ls = []
    test_init(test_ls)

    new_list = get_list_apartment_expenses(test_ls, 2)
    assert len(new_list) == 3

    new_list = get_expense_list_operator(test_ls, '=', 32)
    assert new_list[0] == 1

    new_list = get_expense_list_operator(test_ls, '>', 300)
    assert new_list[0] == 3 and new_list[1] == 7

    new_list = get_expense_list_operator(test_ls, '<', 10000)
    assert len(new_list) == 5

    try:
        get_expense_list_operator(test_ls, '?', 10)
        assert False
    except ValueError:
        assert True


def test_all():
    test_create_expense()
    test_add()
    test_find_expense()
    test_remove()
    test_replace()
    test_total_expenses()
    test_list_func()

if __name__ == '__main__':
    test_all()
    start_command_ui()

