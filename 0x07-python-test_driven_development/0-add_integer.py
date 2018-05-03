#!/usr/bin/python3
def add_integer(a, b=98):
    """
    add_integer - We will be adding two integers

    Args:
    a - first variable
    b - second variable
       - b is set to 98

    Return:
    the addition of a & b

    """

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")

    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
