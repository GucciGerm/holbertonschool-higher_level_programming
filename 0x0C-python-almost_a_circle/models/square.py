#!/usr/bin/python3
"""
    square.py
"""
from models.rectangle import Rectangle
"""
importing the rectangle instance from models/rectangle
"""


class Square(Rectangle):
    """
    class - Here we are creating a class instance
    Square - Here we are creating a square class

    Args:
    Rectangle - This is the class we will be inheriting from

    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        __init__ - class constructor

        Args:
        size - This is the size of the square also taking
        the place of width and height

        x - Horizontal
        y- Vertical
        id - identification
        """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        __str__ - string representation

        """

        return ("[Square] {} {}/{} - {}".format(self.id, self.x,
                                                self.y, self.height))

    @property
    def size(self):
        return (self.width)

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        update - This will assign an argument to each attribute

        Args:
        args - arguments being passed

        """

        attributes = ["id", "size", "x", "y"]

        for tributes in range(len(args)):
            if args[tributes] is not 0:
                setattr(self, attributes[tributes], args[tributes])

        for key in attributes:
            if key in kwargs and kwargs[key] is not None:
                setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """
        to_dictionary - This will return the dictionary representation
        of a square

        """
    def to_dictionary(self):
        """
        to_dictionary - Here we are creating the dictionary representation
        of our rectangle we created

        """

        rectanglevals = ["id", "size", "size", "x", "y"]
        dictionary = {}

        for key in rectanglevals:
            dictionary[key] = getattr(self, key)
        return dictionary
