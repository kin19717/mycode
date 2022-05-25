#!/usr/bin/env python3

def main(): 
    print('How many years have you been an employee: ')
    emyears = int(input())

    if emyears >= 30: #if emyears is greater than or equal to 5
        vacaday = emyears * 3
    elif emyears >=20 :
        vacaday = emyears * 2
    elif emyears >=10 :
        vacaday = emyears * 1.5
   # if emyears < 5:
    else: # this could be read, "in all other cases"
        vacaday = emyears * 1
    print('You have', vacaday, 'vacation days.')


main()
