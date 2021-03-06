#!/usr/bin/python3
import json
"""
Here we are importing the json functions
"""


def from_json_string(my_str):
    """
    from_json_string - This will return an object represented by a Json
    string

    Args:
    my_str - This is the string we're passing

    Return:
    We will return an object represented by json

    """

    return (json.loads(my_str))
