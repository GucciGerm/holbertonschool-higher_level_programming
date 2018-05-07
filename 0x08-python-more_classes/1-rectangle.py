#!/usr/bin/python3
class Rectangle:
    """ Creating a rectangle class """
    def __init__(self, width=0, height=0):
        """
        init allows us to create an instance
        and gave it attributes like width(set to 0) and height(set to 0).
        We accounted for exceptions like if like if the width/height are ints
        and if the width/height is less than 0.

        Args:
        width - is how wide it is
        height - is how tall is it

        Return:
        None
        """
        if type(width) != int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

        if type(height) != int:
            raise TypeError("height must be an integer")
        elif  height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

        @property
        def width(self):
            """
            width - this is how wide the rectangle is

            Args:
            self - this allows an object to refer to itself

            Return:
            We will be returning the width
            """

            return self.__width
        @width.setter
        def width(self, value):
            """
            width - this is how wide the rectangle is

            Args:
            self - this allows an object to refer to itself
            value - this is what it's worth

            Return:
            We will set the property of the width
            """

            if type(value) != int:
                raise TypeError("width must be an integer")
            elif value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value

        @property
        def height(self):
            """
            height - this is how tall the rectangle is

            Args:
            self - this allows an object to refer to itself

            Return:
            We will be returning the height
            """

            return self.__height

        @height.setter
        def height(self, value):
            """
            height - this is how tall the rectangle is

            Args:
            self - this allows an object to refer to itself
            value - this is what it's worth

            Return:
            We will set the property of the height
            """

            if type(value) != int:
                raise TypeError("height must be an integer")
            if height < 0:
                raise ValueError("height must be >= 0")
            self.__height = value
