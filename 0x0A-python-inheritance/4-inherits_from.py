#!/usr/bin/python3
def inherits_from(obj, a_class):
    """
    inherits_from - This function will check if object class is an instance
    of a class that inherited (directly or indirectly) from a specified class

    Args:
    obj - This is the object that we're comparing to see if instance
    a_class - This is the specific class we're checking to see if inherited
    from

    Return:
    The checking of the type of obj will return True, if not Return False
    """

    if type(obj) != a_class:
        return issubclass(type(obj), a_class)
    else:
        return False
