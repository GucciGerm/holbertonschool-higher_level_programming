#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)
    my_list.sort()    # reason for using sort() is we want to sort (my_list)
    return (my_list[-1])    # -1 means you getting the opposite, sort low2high
