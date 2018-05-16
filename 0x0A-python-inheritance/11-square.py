#!/usr/bin/python3

Rectangle = __import__("9-rectangle").Rectangle

"""
Here we are going to import the 9-rectangle into our function
"""
class Square(Rectangle):
    """
    Created a class named Square

    Args:
    Rectangle - This is what we're importing

    Return:
    None
    """

    def __init__(self, size):
        """
        We going to going to give our class attributes like size!

        Args:
        size - is how big the square is

        Return:
        [Square] <width> / <height>
        """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        Here we are returning the string representaiton of our square

        Return:
        This will return [Square] width / height
        """

        return ("[Square] {}/{}".format(self.__size, self.__size))
