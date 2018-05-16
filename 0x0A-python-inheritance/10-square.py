#!/usr/bin/python3

Rectangle = __import__("9-rectangle").Rectangle

"""
We are importing the 9-rectangle function
"""


class Square(Rectangle):
    def __init__(self, size):
        """
        Here we are initializing the size attribute

        Args:
        size - This is the size of the Square

        Return:
        None
        """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return ("[Square] <width>/<height>".format(size))
