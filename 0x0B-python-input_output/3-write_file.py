#!/usr/bin/python3
def write_file(filename="", text=""):
    """
    write_file - Here this function will write a string to a text file
    and return the number of characters written

    Args:
    filename - This is the files name
    text - This is the text we will convert

    Return:
    We will return our alias n in written mode to return # of characters
    """

    with open(filename, mode="w", encoding="utf-8") as n:
        return (n.write(text))
