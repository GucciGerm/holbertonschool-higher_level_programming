#!/usr/bin/python3
import json
"""
Here we will be importing the json functions
"""


def load_from_json_file(filename):
    """
    load_from_json_file - Here we will create an object from the JSON file

    Args:
    filename - This is the file name that we will be altering

    Return:
    We will return our Json created object
    """

    with open(filename, encoding="utf-8") as n:
        return (json.load(n))
