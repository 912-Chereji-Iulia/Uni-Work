#
# Implement the program to solve the problem statement from the second set here
#problem number 10
def read(x):
    x=int(input("Insert a number"))
    return x
def palindrom(x):
    result=0
    while x>0:
        result=result*10+int(x%10)
        x=int(x/10)
    return result
x=0
x=read(x)
print(f"The palindrome of {x} is {palindrom(x)}")