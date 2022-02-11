"""
Tests for functions are here
"""
from src.domain.entity import set_up, create_apartment_expense, get_expense_amount, \
    create_expense_list, get_expenses_values
from src.functions.functions import add_expense, find_expense, get_expense_index, remove_apartment_expenses, \
    remove_apartments_expenses, remove_type_expense, replace_expense, total_expenses_apartment, \
    get_apartment_expenses_list, get_expenses_by_operator_and_value, undo_expenses, get_sum_of_expense_type, \
    get_max_apartment_expense, sort_apartments_by_expenses, sort_expense_types, filter_by_expense_type, filter_by_value


def test_init(test_ls):
    # use this function to add the 10 required items
    # use it to set up test data
    set_up(get_expenses_values(test_ls))


def test_create_expense():
    # Tests create_apartment_expense

    create_apartment_expense([1, 'gas', 10])
    create_apartment_expense(['1', 'gas', 10])

    try:
        create_apartment_expense(['a', 'gas', '10'])
    except ValueError:
        assert True

    try:
        create_apartment_expense(['1', 'air', '10'])
    except ValueError:
        assert True

    try:
        create_apartment_expense(['1', 'gas', '-10'])
    except ValueError:
        assert True

    try:
        create_apartment_expense(['1', 'gas', 10.747])
    except ValueError:
        assert True


def test_add():
    # Tests adding to the list functionality
    test_ls = create_expense_list()
    auxiliary = create_apartment_expense(['15', 'gas', '20'])
    add_expense(test_ls, auxiliary)

    # Checks adding a normal element
    assert len(get_expenses_values(test_ls)) == 11

    auxiliary = create_apartment_expense(['1', 'gas', '20'])
    add_expense(test_ls, auxiliary)

    # Checks adding a new amount to an old element
    assert len(get_expenses_values(test_ls)) == 11

    auxiliary = create_apartment_expense(['20', 'water', '30'])
    add_expense(test_ls, auxiliary)

    assert len(get_expenses_values(test_ls)) == 12


def test_find_expense():
    # Checks the finding functions
    test_ls = create_expense_list()
    test_init(test_ls)
    test_ls_val = get_expenses_values(test_ls)

    aux = find_expense(test_ls_val, 'gas', 'type')
    assert len(aux) == 2

    aux = find_expense(test_ls_val, '1', 'id')
    assert len(aux) == 3

    aux = find_expense(test_ls_val, '100', 'id')
    assert aux is None

    expense = test_ls_val[0]
    aux = get_expense_index(test_ls_val, expense)
    assert aux == 0


def test_remove_apartment_expenses():
    # Checks the remove apartment expenses functions
    test_ls = create_expense_list()

    test_init(test_ls)
    remove_apartment_expenses(test_ls, 1)
    assert len(get_expenses_values(test_ls)) == 7

    test_init(test_ls)
    remove_apartments_expenses(test_ls, 1, 10)
    assert len(get_expenses_values(test_ls)) == 0

    try:
        remove_apartment_expenses(test_ls, 147.7)
        assert False
    except ValueError:
        assert True


def test_remove_type():
    # Checks the remove by type function
    test_ls = create_expense_list()

    test_init(test_ls)
    remove_type_expense(test_ls, 'gas')
    assert len(get_expenses_values(test_ls)) == 8

    try:
        remove_type_expense(test_ls, 'air')
        assert False
    except ValueError:
        assert True


def test_replace():
    # Tests the replace function
    test_ls = create_expense_list()
    test_init(test_ls)

    aux = create_apartment_expense(['1', 'gas', '30'])
    replace_expense(test_ls, aux)

    assert get_expense_amount(aux) == 30

    try:
        # Try to replace an expense which does not exist
        aux = create_apartment_expense([100, 'water', 10])
        replace_expense(test_ls, aux)
        assert False
    except ValueError:
        assert True


def test_total_expenses():
    # Tests the total expenses function
    test_ls = create_expense_list()
    test_init(test_ls)
    test_ls_val = get_expenses_values(test_ls)

    aux = create_apartment_expense([10, 'gas', 20])

    assert total_expenses_apartment(test_ls_val, 1) == 32

    add_expense(test_ls, aux)

    assert total_expenses_apartment(test_ls_val, 10) == 20


def test_list_func():
    # Tests the list functions
    test_ls = create_expense_list()
    test_init(test_ls)

    new_list = get_apartment_expenses_list(test_ls, 1)
    assert len(new_list) == 3

    new_list = get_expenses_by_operator_and_value(test_ls, '=', 32)
    assert new_list[0] == 1

    new_list = get_expenses_by_operator_and_value(test_ls, '<', 10000)
    assert len(new_list) == 5

    new_list = get_expenses_by_operator_and_value(test_ls, '>', 300)
    assert new_list[0] == 3 and new_list[1] == 7

    try:
        get_expenses_by_operator_and_value(test_ls, '?', 10)
        assert False
    except ValueError:
        assert True


def test_sum():
    # Tests the sum function
    test_ls = create_expense_list()
    test_init(test_ls)
    t_sum = get_sum_of_expense_type(test_ls, 'other')
    assert t_sum == 530

    try:
        get_sum_of_expense_type(test_ls, 'air')
        assert False
    except ValueError:
        assert True


def test_max():
    # Tests the max function
    test_ls = create_expense_list()
    test_init(test_ls)

    assert get_max_apartment_expense(test_ls, 1) == 20

    try:
        get_max_apartment_expense(test_ls, 10.5)
        assert False
    except ValueError:
        assert True


def test_sort_by_apartment_expense():
    # Tests the sort by apartments and expenses function
    test_ls = create_expense_list()
    test_init(test_ls)

    # Sort by apartment and total expenses
    sorted_list = sort_apartments_by_expenses(test_ls)

    assert len(sorted_list)
    assert sorted_list[0] == (1, 32)

    remove_apartment_expenses(test_ls, 1, 7)
    sorted_list = sort_apartments_by_expenses(test_ls)
    assert sorted_list[0] == (4, 120)




def test_sort_by_type():
    # Tests the sort by type function
    test_ls = create_expense_list()
    test_init(test_ls)

    # Sort by type
    test_init(test_ls)
    sorted_list = sort_expense_types(test_ls)

    assert sorted_list[0] == ('water', 30)

    remove_type_expense(test_ls, 'water')
    sorted_list = sort_expense_types(test_ls)
    assert sorted_list[0] == ('electricity', 210)




def test_filter_by_expense_type():
    # Tests the filter by expense function
    test_ls = create_expense_list()
    test_init(test_ls)

    filter_by_expense_type(test_ls, 'gas')
    assert len(get_expenses_values(test_ls)) == 2

    try:
        filter_by_expense_type(test_ls, 'water')
        assert False
    except ValueError:
        assert True

    try:
        filter_by_expense_type(test_ls, 'air')
        assert False
    except ValueError:
        assert True

    remove_type_expense(test_ls, 'gas')
    try:
        filter_by_expense_type(test_ls, 'gas')
        assert False
    except ValueError:
        assert True


def test_filter_by_value():
    # Tests the filter by value function
    test_ls = create_expense_list()
    test_init(test_ls)

    filter_by_value(test_ls, 200)
    assert len(get_expenses_values(test_ls)) == 6

    try:
        filter_by_value(test_ls, 100.5)
        assert False
    except ValueError:
        assert True

    try:
        filter_by_value(test_ls, 1)
        assert False
    except ValueError:
        assert True

    remove_apartments_expenses(test_ls, 1, 10)
    try:
        filter_by_value(test_ls, 50)
        assert False
    except ValueError:
        assert True


def test_undo():
    # Tests the undo function
    test_ls = create_expense_list()
    test_init(test_ls)

    # Adds a new expense to the lists and undoes it
    add_expense(test_ls, create_apartment_expense([1, 'gas', 200]))
    undo_expenses(test_ls)
    new_test_ls = create_expense_list()
    test_init(new_test_ls)
    assert test_ls == new_test_ls

    try:
        undo_expenses(test_ls)
        assert False
    except ValueError:
        assert True


def test_all():
    test_create_expense()
    test_add()
    test_find_expense()
    test_remove_apartment_expenses()
    test_remove_type()
    test_replace()
    test_total_expenses()
    test_list_func()
    test_sum()
    test_max()
    test_sort_by_apartment_expense()
    test_sort_by_type()
    test_filter_by_expense_type()
    test_filter_by_value()
    test_undo()