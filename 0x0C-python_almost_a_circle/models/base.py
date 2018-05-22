#!/usr/bin/python3
import json


class Base:
    """
    class - Here we are creating a class
    Base - Here we are creating a base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        __init__ - class constructor

        Args:
        id - Set to id to none, this is the instance's identification

        """

        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def validator(name, value):
        """
        validator - This will validate the value to see if
        they are of the correct type

        Args:
        name - (You can assume this is a string)
        value - This is what we're validating

        Return:
        None

        """

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if name is "width" or name is "height":
            if value < 0:
                raise ValueError("{} must be > 0".format(name))
        if name is "x" or name is "y":
            if value < 0:
                raise ValueError("{} must be >= 0".format(name))

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        to_json_string - This will return the JSON string representation
        of list_dictionaries

        Args:
        list_dictionaries - This is a list of directories

        """

        if list_dictionaries is None:
            return ("[]")
        else:
            return json.dumps(list_dictionaries)
