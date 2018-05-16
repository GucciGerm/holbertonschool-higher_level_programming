#!/usr/bin/python3

BaseGeometry = __import__("7-base_geometry").BaseGeometry
"""
Here we are importing the 7-base_geometry function into our class
"""

class Rectangle(BaseGeometry):
    """
    Creating a Rectangle class that can inherit from basegeometry
    """

    def __init__(self, width, height):
        """
        intializing the integer validator by calling it in using super

        Args:
        width - Horizontal
        Height - Vertical

        Return:
        None
        """

        super().integer_validator("width", width)
        super().integer_validator("height", height)

        self.__width = width
        self.__height = height
