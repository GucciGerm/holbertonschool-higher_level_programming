#!/usr/bin/python3
import json

"""
Here we are importing the json funcs
"""


def to_json_string(my_obj):
    """
    to_json_string - This will return the JSON representation of
    a (string)object

    Args:
    my_obj - This is the obj we are passing

    Return:
    We will return the JSON representation of a string
    """
    return (json.dumps(my_obj))
