#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """
    say_my_name -
    This function will print "My name is <first><last>"

    Args:
    first_name - is the users first name
    last_name - is the users last name

    Return:
    None

    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")

    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print ("My name is {} {}".format(first_name, last_name))
