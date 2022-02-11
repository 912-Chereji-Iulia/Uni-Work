"""
    Service class includes functionalities for implementing program features
"""
from src.domain.entity import expense
import copy
import random
class expenses_list:
    """
    create a list of expenses
    """
    def __init__(self, expenses= False):
        self._expenses= []
        self._history = []
        if expenses:
            expenses_type = ['water', 'gas', 'electricity', 'food', 'other']
            for i in range(10):
                day = random.randint(1, 30)
                amount = random.randint(0, 1000)
                type = random.choice(expenses_type)
                exp = expense(day, amount, type)
                self._expenses.append(exp)


    def search_expense(self, exp):
        """
        returns the index of an expense with the same day and type if found
        :param exp:
        :return:
        """
        for i in range(len(self._expenses)):
            if self._expenses[i].day == exp.day and self._expenses[i].expense_type == exp.expense_type:
                return i
        return None


    def add_expense(self, exp):
        """
        we add the expense to the list
        :param expense:
        :return:
        """
        index=self.search_expense(exp)
        old_values = copy.deepcopy(self._expenses)
        self._history.append(old_values)
        if index is None:
            self._expenses.append(exp)
        else:
            self._expenses[index].amount += exp.amount

    def get_expenses(self):
        """
        return the expenses_list expenses
        :return:
        """
        return self._expenses

    def filter_expense(self, val):
        """
        removes any expense from the list which has a value less than val
        :param val:
        :return:
        """
        try:
            val=int(str(val))
            if val < 0:
                raise ValueError
        except ValueError:
            raise ValueError("{} needs to be a positive integer".format(val))

        old_expense=copy.deepcopy(self._expenses)
        self._history.append(old_expense)

        bad_expenses=[]
        for exp in self._expenses:
            if exp.amount <= val:
                bad_expenses.append(exp)
        for exp in bad_expenses:
            self._expenses.remove(exp)


    def undo(self):
        """
        Undoes the last operation
        :return:
        """
        if len(self._history) == 0:
            raise IndexError('Cannot undo operation!')

        old_form =self._history.pop()
        self._expenses.clear()
        self._expenses = old_form

