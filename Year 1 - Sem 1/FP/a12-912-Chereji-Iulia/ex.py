def consistent(n,list):
    """
    Determines whether the current partial array can lead to a solution
    """
    open = 0
    closed = 0
    for i in range(len(list)):
        if list[i] == 0:
            open += 1
        else:
            closed += 1
    if open <= n//2 and closed <= open:
        return True
    return False


def solution(list, n):
    """
    Determines whether we have a solution
    """
    return len(list) == n


def print_parentheses(list):
    l = []
    for i in list:
        if i == 0:
            l.append("(")
        elif i ==1:
            l.append(")")
    print("".join(l))


def next_element(list):
    """
    decides which type of paranthesis is next
    :param list:
    :return:
    """
    if list[-1] == 1:
        return None
    return list[-1] + 1


def bkt_recursive(n, list):
    """
    Backtracking algorithm, recursive implementation
    """
    list.append(0)
    elem = 0
    while elem is not None:
        if consistent(n,list):
            if solution(list, n):
                print_parentheses(list)
            else:
                copy = list[:]
                bkt_recursive(n, copy)
        elem = next_element(list)
        list[-1] = elem


def bkt_iterative(n):
    """
    Backtracking algorithm, iterative implementation
    :param n: the nr of parentheses
    :return:
    """
    list = [-1]
    while len(list) > 0:
        elem = next_element(list)
        while elem is not None:
            list[-1] = elem
            if consistent(n, list):
                if solution(list, n):
                    print_parentheses(list)
                else:
                    list.append(-1)
                    break
            elem = next_element(list)
        if elem is None:
            list.pop()


def start():
    done = False
    list1=[]
    while not done:
        sol=input("iterative or recursive? >>>")
        if sol.lower()=='recursive':
            n = int(input("Enter the number of parentheses: "))
            if n%2 == 0:
                done = True
                bkt_recursive(n, list1)
            else:
                print("\033[35mYou can't close correctly an odd number of parantheses. Please enter an even number!\033[0m")
        elif sol.lower()=='iterative':
            n = int(input("Enter the number of parentheses: "))
            if n % 2 == 0:
                done = True
                bkt_iterative(n)
            else:
                print("\033[35mYou can't close correctly an odd number of parantheses. Please enter an even number!\033[0m")
        else:
            print("\033[35mBad input\033[0m")

start()
