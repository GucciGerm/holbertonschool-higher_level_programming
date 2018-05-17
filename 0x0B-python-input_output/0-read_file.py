#!/usr/bin/python3
def read_file(filename=""):
    """
    read_file - Here this function will read a text file (UTF8)
    and prints it as the standardoutput

    Args:
    filename - this is the file name

    Return:
    None, print back the text file

    """

    with open(filename, encoding="utf-8") as n:
            print(n.read(), end="")
