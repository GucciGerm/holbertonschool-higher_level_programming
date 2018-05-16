#!/usr/bin/python3

BaseGeometry = __import__("7-base_geometry").BaseGeometry

"""
Here we are importing the 7-base_geometry function into our rectangle
"""


class Rectangle(BaseGeometry):
    """
    Created a rectangle class that inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """
        Giving the rectangle attributes

        Args:
        width - Horizontal (how wide)
        height - Vertival (how tall)

        Return:
        str() should return [Rectangle] <width> / <height>

        """

        self.integer_validator = width
        self.integer_validator = height
        self.__width = width
        self.__height = height

    def area(self):
        """
        This will return the area of the rectangle

        Return:
        This will return the width * height
        """
        return ((self.__width) * (self.__height))

    def __str__(self):
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
