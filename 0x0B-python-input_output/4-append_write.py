#!/usr/bin/python3
def append_write(filename="", text=""):
    """
    append_write - This function will append a string to the end of our
    text file

    Args:
    filename - This is our file name
    text - This is the text we will convert

    Return:
    This function will return the number of characters added
    """
    with open(filename, mode="a", encoding="utf-8") as n:
        return (n.write(text))
