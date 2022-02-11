"""
    UI class.

    Calls between program modules
    ui -> service -> entity
    ui -> entity
"""
from src.services.service import expenses_list

from src.domain.entity import expense

class UI:
    def __init__(self):
        self._expenses = expenses_list(True)

    def add_ui(self, expenses ):
        day = input("Enter a day: ")
        amount = input("Enter the amount: ")
        type = input("Enter the expense type: ")
        exp = expense(day, amount, type)
        self._expenses.add_expense(exp)
        print("Added!\n")


    def display_ui(self,expenses):
        expense_list = self._expenses.get_expenses()
        if len(expense_list):
            for exp in expense_list:
                print(exp)
        else:
            print("There are no expenses!")
        print ('\n')


    def filter_ui(self, val):
        val= input("Enter the value: ")
        self._expenses.filter_expense(val)
        print ('Filtered \n')


    def undo_ui(self, expenses):
        self._expenses.undo()
        print ('The last operation was undid! \n')


    def print_menu(self):
        print("1.Add an expense")
        print("2.Display the list of expenses")
        print("3.Filter the list so that it contains only expenses above a certain value.")
        print("4.Undo the last operation")
        print("5.Exit")


    def start_ui(self):
        expense_list = self._expenses
        done=False
        command_dict={'1' : self.add_ui, '2' : self.display_ui, '3' : self.filter_ui, '4' : self.undo_ui}
        while not done:
            self.print_menu()
            cmd = input("Enter the command: ")
            try:
                if cmd in command_dict:
                    command_dict[cmd](expense_list)
                elif cmd == '5':
                    print('Bye bye!')
                    done = True
                else:
                    print("Invalid command \n")
            except Exception as exc:
                print(str(exc) + '\n')

