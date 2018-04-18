#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    trueorfalse = []
    for n in my_list:
        if n % 2 == 0:
            trueorfalse.append(True)
        if n % 2 != 0:
            trueorfalse.append(False)
    return (trueorfalse)
