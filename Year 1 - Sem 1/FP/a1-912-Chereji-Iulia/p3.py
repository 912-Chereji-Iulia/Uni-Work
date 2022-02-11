#
# Implement the program to solve the problem statement from the third set here
#problem number 12
def leap_year(y): #we check if a year is a leap one
    if y%400==0:
        return True
    if y%100==0 :
        return False
    if y%4==0:
        return True
    return False
def nr_leap(y): #we calculate the number of leap years between year 1 and the y year
    return (y//4)-(y//100)+(y//400)
def date_to_days(y,mo,d): # we calculate the number of days since day 1, year 1
    days=0
    leapyears=leap_year(y-1)
    days=366*leapyears+365*(y-1-leapyears)
    for m in range(1,mo):
        if(m==2):
            days=days+28
            if leap_year(y):
                days=days+1
        elif m in [1, 3, 5, 7, 8, 10, 12]:
            days=days+31
        else:
            days=days+30
    days=days+d
    return days
yb=int(input("Insert your birth year"))
mb=int(input("Insert your birth month"))
db=int(input("Insert your birth day"))
yc=int(input("Insert the current year"))
mc=int(input("Insert the current month"))
dc=int(input("Insert the current day"))
bdays=date_to_days(yb,mb,db)
cdays=date_to_days(yc,mc,dc)
print(f"You are {cdays-bdays+1} days old")



