#
# Implement the program to solve the problem statement from the first set here
#problem number 2
def read(n):
    n=int(input("Insert a number"))
    return n
def prime_number(x): #we check if a given number is prime
    if x<2:
        return False
    if x==2:
        return True
    if x%2==0:
        return False
    d=3
    while d*d<=x:
        if x%d==0:
            return False
        d=d+1
    return True
def Goldbach(x):
    if x%2==0: #we find the middle of the number, distinguishing 2 cases: when x is even and odd
        j1=int(x/2)
    else:
        j1=int((x-1)/2)
    j2=x-j1
    while not prime_number(j1) or not prime_number(j2):
        j1=j1-1
        j2=j2+1
        if j1<=1:
          break

    if j1<=1:
       print("There are no prime numbers that can satisfy the condition")
    else:
       print(f"The prime numbers that have the sum equal to {x} are {j1} and {j2}")

n=0
n=read(n)
Goldbach(n)
