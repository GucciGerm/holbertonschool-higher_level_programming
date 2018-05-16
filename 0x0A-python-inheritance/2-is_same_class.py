#!/usr/bin/python3
def is_same_class(obj, a_class):
    """
    is_same_class - This function will check true or false if
    an object is exactly an instance of the specified class

    Args:
    obj - This is the object we're checking to see if is an exact instance
    a_class - This is the class that we are to see if the object is instance

    Return:
    True if the object is an instance or return False if the object is not
    """

    if isinstance(obj, a_class):
        return (True)
    else:
        return (False)
