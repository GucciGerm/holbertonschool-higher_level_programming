#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    """
    is_kind_of_class - This function will check if the object is an instance
    of or if the object is an exact instance of a class inherited
    the specifc class

    Args:
    obj - This is the obj we will be checking to see if instance
    a_class - This is the class we will be comparing to obj

    Return:
    True if the obj is an instance or specfic instance of a_class
    False if the obj is not an instance
    """

    if isinstance(obj, a_class):
        return True
    else:
        return False
