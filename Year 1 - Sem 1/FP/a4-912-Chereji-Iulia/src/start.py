"""
Assemble the program and start the user interface here
"""
from src.domain.entity import create_expense_list
from src.test.tests import test_all
from src.ui.console import add_command_ui, remove_command_ui, replace_command_ui, display_command_ui, split_commands, undo_ui, sum_ui, max_ui, sort_ui, filter_ui


def cmd_menu():
    print("Possible commands: add, remove, replace, list, sum, max, sort, filter, undo, exit")

    expenses = create_expense_list()
    done = False

    command_dict = {'add': add_command_ui, 'remove': remove_command_ui, 'replace': replace_command_ui,
                    'list': display_command_ui, 'sum': sum_ui, 'max': max_ui, 'sort': sort_ui, 'filter': filter_ui,
                    'undo': undo_ui}

    while not done:
        try:
            # getting input
            command = input('>>>command ').strip()

            command_word, command_params = split_commands(command)

            if command_word == 'exit':
                # Exits the program
                done = True
            elif command_word in command_dict:
                command_dict[command_word](expenses, command_params)
            else:
                print('Bad Command')

        except ValueError as ve:
            print(str(ve))


test_all()
cmd_menu()