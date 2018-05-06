#!/usr/bin/python3
def print_square(size):
    if size < 0:
        raise ValueError("size msut be >= 0")
    if (isinstance(size, float)) < 0:
        raise TypeError("size must be an integer")
    if type(size) != int:
        raise TypeError("size must be an integer")

    for row in range(size):
        for colum in range(size):
            print ("#", end="")
        print()
