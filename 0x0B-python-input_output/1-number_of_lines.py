#!/usr/bin/python3
def number_of_lines(filename=""):
    """
    number_of_lines - This functions will return the number of lines
    in a text file

    Args:
    filename - this is our filename that we will be checking

    Return:
    We will return the number of lines in our text file
    """
    with open(filename) as n:
        for lines, count in enumerate(n):
            pass
        return (lines + 1)
