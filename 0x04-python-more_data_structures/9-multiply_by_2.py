#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    n = a_dictionary.copy()
    for key in a_dictionary:
        n[key] = a_dictionary[key] * 2
    return n
