
def prim(n):
    '''
    we check if a given number is prime
    :param n: the given number
    :return: True if it is prime or False otherwise
    '''
    if n<2:
        return False
    if n==2: 
        return True
    if n%2==0: 
        return False

    for d in range(3,n,2):
        if n%d==0:
            return False

    return True

def sum(l,st,dr):
    """
    using Divide et impera, we divide the problem in smaller sub-problems
    we begin with st=0 and dr=len(l)-1 and we continuosly compute the middle of the parts
    of the list and call, recursiively, the function
    when we reach st equal to dr we check if the position is prime
    :param l: the given list
    :param st: the left limit of the list
    :param dr: the right limit of the list
    :return: the sum of numbers on prime positions
    """

    if st == dr:
        if prim(st):
            return l[st]
        else:
            return 0
    else:
        mij = (st+dr)//2
        return sum(l, st, mij)+sum(l, mij+1, dr)



def test_sum():
    '''
    we test the function sum
    :return:
    '''
    l = [1,2,3,4,5]
    assert sum(l, 0, 4) == 7

    l = [2,3]
    assert sum(l, 0, 1) == 0

    l = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    assert sum(l, 0, 14) == 71

    l=[]
    assert sum(l,0,0) == 0

def test_prime():
    '''
    we test the prim function
    :return: 
    '''
    assert prim(7)==True
    assert prim(2)==True
    assert prim(6)==False
    assert prim(0) == False
    assert prim(1) == False
    assert prim(15)== False

l=[]
print(sum(l,0,0))