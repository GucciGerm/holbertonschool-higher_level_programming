#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    a_dictionary.pop('key', None)
    a_dictionary.pop('track', None)
    return a_dictionary
