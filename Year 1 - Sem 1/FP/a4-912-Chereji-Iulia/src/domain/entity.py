"""
Domain file includes code for entity management
entity = number, transaction, expense etc.
"""


def check_int(value):
    """
    Raises a ValueError if value is not an integer
    :param value: Value
    """
    try:
        value = int(str(value))
        if value <= 0:
            raise ValueError
    except ValueError:
        raise ValueError('{} should be a positive integer'.format(value))


def check_expense_type(value):
    """
    Raises a ValueError if value is not an expense type ('water', 'heating', 'electricity', 'gas', 'other')
    :param value: Value
    """
    try:
        if value not in ['water', 'heating', 'electricity', 'gas', 'other']:
            raise ValueError
    except ValueError:
        raise ValueError("{} should be a valid expense type (water, heating, electricity, gas, other)".format(value))


def set_up(expenses):
    """
    Adds 10 elements to the expense list
    :param expenses: List of expenses
    """
    expenses.clear()
    expenses.append(create_apartment_expense(['1', 'gas', '20']))
    expenses.append(create_apartment_expense(['2', 'water', '30']))
    expenses.append(create_apartment_expense(['1', 'other', '10']))
    expenses.append(create_apartment_expense(['3', 'electricity', '200']))
    expenses.append(create_apartment_expense(['2', 'gas', '250']))
    expenses.append(create_apartment_expense(['3', 'heating', '280']))
    expenses.append(create_apartment_expense(['4', 'heating', '120']))
    expenses.append(create_apartment_expense(['7', 'other', '520']))
    expenses.append(create_apartment_expense(['2', 'electricity', '10']))
    expenses.append(create_apartment_expense(['1', 'heating', '2']))
    # totals: 1 - 32, 2 - 290, 3 - 480, 4 - 120, 7 - 520


def get_expenses_values(expenses):
    return expenses['values']


def set_expenses_values(expenses, val):
    expenses['values'] = val


def get_expenses_history(expenses):
    return expenses['history']


def create_expense_list():
    expenses = {'values' : [], 'history': []}
    set_up(get_expenses_values(expenses))
    return expenses


def create_apartment_expense(arg):
    """
    Creates a new expense
    Raises ValueError if arg is not valid (incorrect length or types are wrong)
    :param arg: Expense arguments (List of 3)
    :return: A new expense (Dictionary)
    """
    # Error handling
    if len(arg) != 3:
        raise ValueError('Expense cannot be created: not enough arguments')
    check_int(arg[0])
    check_expense_type(arg[1])
    check_int(arg[2])

    ap_id = int(arg[0])
    expense_type = str(arg[1])
    amount = int(arg[2])
    return {'ap_id': ap_id, 'expense_type': expense_type, 'amount': amount}


def get_expense_apartment(expense):
    return expense['ap_id']


def set_expense_apartment(expense, value):
    expense['ap_id'] = value


def get_expense_type(expense):
    return expense['expense_type']


def set_expense_type(expense, value):
    expense['expense_type'] = value


def get_expense_amount(expense):
    return expense['amount']


def set_expense_amount(expense, value):
    expense['amount'] = value