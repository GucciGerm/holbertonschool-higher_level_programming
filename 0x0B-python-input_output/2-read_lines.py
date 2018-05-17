#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    """
    read_lines - This function will read n lines of a textfile
    and print to the standardoutput

    Args:
    filename - This is the name of the file
    nb_lines - This is the number of lines

    Return:
    None, Will will respected amount of file
    """
    num = 0
    with open(filename, mode="r", encoding="utf-8") as n:
        if nb_lines <= 0:
            print(n.read(), end="")
        else:
            for n in n:
                if num < nb_lines:
                    print(n, end="")
                num += 1
