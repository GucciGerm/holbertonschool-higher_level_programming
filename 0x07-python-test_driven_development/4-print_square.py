#!/usr/bin/python3

"""
print square function - Here this will print a square
"""

def print_square(size):
    """
    print_square will print a square by using the "#" character by size
    """

    if size < 0:
        raise ValueError("size must be >= 0")
    if (isinstance(size, float)) and size < 0:
        raise TypeError("size must be an integer")
    if (isinstance(size, int):
        raise TypeError("size must be an integer")

    for row in range(size):
        for colum in range(size):
            print ("#", end="")
        print()
