#!/usr/bin/python3
def no_c(my_string):
    var = ''
    for n in my_string:
        if n == 'c' or n == 'C':
            n = ''
        var = var + n
    return var
