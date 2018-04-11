#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = -number  # flip the number if negative
    placeholder = number % 10
    print("{}".format(placeholder), end='')  # have the end='' for in line
    return(placeholder)
