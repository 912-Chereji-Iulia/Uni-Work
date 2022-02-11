from src.services.service import expenses_list
from src.domain.entity import expense, ExpenseException

def test_init(test_list):
    test_list.add_expense(expense(2, 100, 'gas'))
    test_list.add_expense(expense(4, 50, 'water'))
    test_list.add_expense(expense(6, 57, 'food'))
    test_list.add_expense(expense(5, 42, 'electricity'))
    test_list.add_expense(expense(4, 85, 'food'))
    test_list.add_expense(expense(3, 350, 'food'))
    test_list.add_expense(expense(4, 400, 'tv'))
    test_list.add_expense(expense(9, 25, 'gas'))
    test_list.add_expense(expense(8, 40, 'heating'))
    test_list.add_expense(expense(10, 60, 'other'))

def test_create_exp():
    test_exp =expense(2,10,'gas')
    assert test_exp.day == 2
    assert test_exp.amount ==10
    assert test_exp.expense_type == 'gas'

    try:
        expense(2.5,23,'gas')
        assert False
    except ExpenseException:
        assert True

    try:
        expense(2, -23,'gas')
        assert False
    except ExpenseException:
        assert True

    try:
        expense(2,23,34)
        assert False
    except ExpenseException:
        assert True

    try:
        expense(31,23,'gas')
        assert False
    except ExpenseException:
        assert True


def test_search():
    test_list = expenses_list()
    test_init(test_list)

    index = test_list.search_expense(expense(6, 57, 'food'))
    assert index == 2

    index = test_list.search_expense(expense(8, 100, 'books'))
    assert index is None

def test_add():
    test_list = expenses_list()
    test_list.add_expense(expense(2,10,'gas'))
    assert test_list.get_expenses()[0].day == 2
    assert test_list.get_expenses()[0].amount == 10
    assert test_list.get_expenses()[0].expense_type == 'gas'


    test_list.add_expense(expense(20, 10, 'gas'))
    assert test_list.get_expenses()[-1].day == 20
    assert test_list.get_expenses()[-1].amount == 10
    assert test_list.get_expenses()[-1].expense_type == 'gas'


    test_list.add_expense(expense(2, 20, 'gas'))
    assert test_list.get_expenses()[0].amount == 30


def test_get_list():
    test_list = expenses_list()
    test_init(test_list)

    assert test_list.get_expenses()[0].day == 2
    assert test_list.get_expenses()[0].amount == 100
    assert test_list.get_expenses()[0].expense_type == 'gas'


def test_filter():
    test_list = expenses_list()
    test_init(test_list)
    test_list.filter_expense(100)
    assert len(test_list.get_expenses()) == 2


def test_undo():
    test_list = expenses_list()
    test_list.add_expense(expense(1, 50, 'heating'))
    test_list.undo()
    assert len(test_list.get_expenses()) == 0


def test_all():
    test_create_exp()
    test_search()
    test_add()
    test_get_list()
    test_filter()
    test_undo()


