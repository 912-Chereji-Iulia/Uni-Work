#
# Write the implementation for A2 in this file
#

# UI section
def print_longest_sequence(my_list, index1, index2):
    """
    we print the longest sequence of a given property between 2 indexes
    :param my_list: the list of the complex numbers
    :param index1: the first index of the interval
    :param index2: the second index of the interval
    :return:
    """
    for i in range(index1, index2):
        print(to_str(my_list[i]))

def longest_real_numbers(my_list):
    """
    we find the longest sequence of real numbers
    :param my_list: the list of complex numbers
    :return:
    """
    max = 0
    maxi = 0
    for index in range(0,len(my_list)):
        length = find_ls_real(my_list, index) - index + 1
        if length > max:
            max = length
            maxi = index

    print(f"The longest sequence of real numbers is between positions {maxi+1} and {maxi + max - 2}: ")
    print_longest_sequence(my_list, maxi+1, maxi + max - 1)



def longest_modulus(my_list):
    """
    we find the longest sequence of numbers that have modulus in the [0, 10] range.
    :param my_list: the list of complex numbers
    :return:
    """
    max = 0
    maxi = 0
    for index in range(0, len(my_list) - 1):
        length = find_ls_modulus(my_list, index) - index + 1
        if length > max:
            max = length
            maxi = index

    print(f"The longest sequence of numbers that have modulus in the [0, 10] range is between positions {maxi} and {maxi + max - 2}: ")
    print_longest_sequence(my_list, maxi, maxi + max - 1)


def read_complex(my_list):
    """
    read a number of complex numbers and then read in a loop all the complex numbers

    :return:
    """
    counter = int(input("Enter a number: "))
    while counter :
        real_part = int(input("Real part: "))
        imaginary_part = int(input("Imaginary part: "))
        my_list.append(create_complex(real_part, imaginary_part))
        counter = counter - 1



def print_menu():
    print('\n')
    print("1 add a complex number")
    print("2 display the complex numbers list")
    print("3 display the longest sequence of real numbers ")
    print("4 display the longest sequence of the numbers with modulus in [0,10] range")
    print("5 exit the application")

def display_list(my_list):
    """
    Display the current list of complex numbers
    :param my_list: the complex numbers list
    :return:
    """
    for complex_number in my_list:
        print(to_str(complex_number))

def start():
    """
    Handle the main menu
    :return: returns once the program is finished
    """
    my_list = []
    init_list(my_list)
    done = False
    command_dict = {'1': read_complex, '2': display_list, '3': longest_real_numbers, '4':longest_modulus}
    while not done:
        print_menu()
        operation = input("Enter operation: ")
        if operation in command_dict:
            command_dict[operation](my_list)
        elif operation == '5':
            print("Exit")
            done = True
        else:
            print("Bad command entered!")


# Function section
# (write all non-UI functions in this section)
# There should be no print or input statements below this comment
# Each function should do one thing only
# Functions communicate using input parameters and their return values

def find_ls_real(my_list, index1):
    """
    we find the longest sequence of real numbers starting from position index1 in the list
    :param my_list:
    :param index1:
    :return:
    """
    done = False
    index2 = index1 + 1
    while not done and (index2 < len(my_list)):
        if my_list[index2]['imag']!=0:
            done = True
        else:
            index2 += 1

    # if number on position index1 is the same as the number on position index2 then the longest sequence would be 1, so in order to do that we substract 1 from index2
    if index1 == index2 - 1:
        index2 -= 1

    return index2


def find_ls_modulus(my_list, index):
    """
    we find the longest sequence of numbers with the modulus in range [0,10]
    :param my_list:
    :param index:
    :return:
    """
    done = False
    while not done and (index < len(my_list) ):

        if get_imag(my_list[index])* get_imag(my_list[index])+get_real(my_list[index])*get_real(my_list[index])>100:
            done = True

        if not done:
            index += 1

    return index


def get_real(complex_number):
    return complex_number['real']


def get_imag(complex_number):
    return complex_number['imag']

def to_str(complex_number):
    return (str(get_real(complex_number)) + ' + (' + str(get_imag(complex_number)) + 'i)')

def create_complex(real_part, imaginary_part = 0):
    """
    Create a real number with a given real and imaginary part and append it to the list
    :param real_part:
    :param imaginary_part:
    :param my_list:
    :return:
    """
    return {'real': real_part, 'imag': imaginary_part}


def init_list(my_list):
    """
    We initialize the list with 10 random complex numbers
    :param my_list: The list where we will store all the complex numbers
    :return:
    """
    my_list.append({'real': -5, 'imag': 0})
    my_list.append({'real': 3, 'imag': 4})
    my_list.append({'real': 2, 'imag': 0})
    my_list.append({'real': 3, 'imag': 0})
    my_list.append({'real': 2, 'imag': 0})
    my_list.append({'real': 2, 'imag': 1})
    my_list.append({'real': 9, 'imag': 0})
    my_list.append({'real': 5, 'imag': 0})
    my_list.append({'real': 12, 'imag': 0})
    my_list.append({'real': 7, 'imag': 0})


start()
