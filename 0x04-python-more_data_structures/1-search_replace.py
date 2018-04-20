#!/usr/bin/python3
def search_replace(my_list, search, replace):
    empty = my_list[:]
    for n in range(len(my_list)):
        if my_list[n] == search:
            empty[n] = replace
    return empty
