#!/usr/bin/python3
def max_integer(my_list=[]):
    holder = my_list[0]
    for n in my_list:
        if n > holder:
            holder = n
    return holder