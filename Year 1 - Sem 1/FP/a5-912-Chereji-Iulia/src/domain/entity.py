"""
    Entity class should be coded here
"""

class ExpenseException(Exception):
    """
    exception class for expense
    """
    def __init__(self,msg):
        self._msg = msg


class expense:
    def __init__(self, day, amount, expense_type):
        """
        Create a new expense
        :param day: integer between 1 and 30
        :param amount: positive integer
        :param expense_ype: string
        """
        try:
            day=int(str(day))
            amount=int(str(amount))
        except ValueError:
            raise ExpenseException("Day and amount need to be integers!")
        if day < 1 or day > 30:
            raise ExpenseException("Day should be between 1 and 30!")
        if amount < 0 :
            raise ExpenseException ("Amount should be a positive integer!")
        if type(expense_type) != str:
            raise ExpenseException("The expense type should be a string")
        self._day = day
        self._amount = amount
        self._expense_type = expense_type
    @property
    def day(self):
        return self._day

    @property
    def amount(self):
        return self._amount

    @property
    def expense_type(self):
        return self._expense_type

    @day.setter
    def day(self, val):
        try:
            val=int(str(val))
            if val<0 or val > 30:
                raise ValueError
        except ValueError:
            raise ExpenseException("Day needs to be an integer between 1 and 30")
        self._day = val

    @amount.setter
    def amount(self, val):
        try:
            val=int(str(val))
            if val<0 :
                raise ValueError
        except ValueError:
            raise ExpenseException("Amount needs to be a positive integer")
        self._amount = val

    @expense_type.setter
    def expense_type(self, val):
        if type(val) != str:
            raise ExpenseException("The expense type needs to be a string")
        self._expense_type = val


    def __str__(self):
        """
        we return the expense in a better format to be printed out
        :return:
        """
        return "day: " + str(self._day) + "| amount: "+ str(self._amount) + "| type: " + str(self._expense_type)


