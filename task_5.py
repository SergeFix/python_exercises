# Functions

import re

# 1. function that returns the multiplication of all input arguments. The function should ignore non-numeric arguments.

def mult_Digits (*args):
    mltDig = 1

    for ii in args:
        if re.search(r'\D+', ii):
            pass
        else:
            mltDig *= int(ii)
    print('func 1:   ' + str(mltDig))

print('func 1 is started')
mult_Digits('qq', 'ww', '4', '5')


# 2. Function that takes a number and returns the sum of its digits.
# \Raise exception if argument of the wrong type was passed

def sum_Digits (*datas):
    sumDig = 0

    for ii in datas:
        try:
            sumDig = sumDig + ii
        except TypeError:
            print(ii + ' is not numeric')
    print('results:  ' + str(sumDig))

print('func 2 is started')
sum_Digits('qq', 'ww', 4, 5)

# 3. Write a function that takes a list of strings AND a minimum length (number)\
#  and returns only the strings that are longer than the provided number.

def sort_by_lenth (*args):
    threshold = args[0]
    text_list = args [1:]
    results = []

    for i in range(len(text_list)):
        if threshold < len(text_list[i]):
            results.append(text_list[i])
    print('func 3:' + str(results))

print('func 3 is started')
sort_by_lenth (3, 'aaa', 'bbbb', 'ccccc', 'd')