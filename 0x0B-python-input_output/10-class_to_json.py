#!/usr/bin/python3
def class_to_json(obj):
    """
    class_to_json - This function will return the dictionary description
    with a simple data structure for JSON serialization of an object

    Args:
    obj - This is the object to get evaluated

    Return:
    We will return the dictionary description wit h a simple data structure
    """

    return (obj.__dict__)
