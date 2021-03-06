#!/usr/bin/python3
class Rectangle:
    """
    Creating a rectangle class and intializing the number of instances
    """
    number_of_instances = 0
    print_symbol = "#"

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
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        Rectangle.number_of_instances += 1

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
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ area is the measure of length x width """

        return self.width * self.height

    def perimeter(self):
        """ here we are finding the parameter """

        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * self.__width + 2 * self.__height

    def __str__(self):
        """ to compute informal or nicely printeable string representation
        of an object
        """
        everynew_rectangle = ""

        if self.__width == 0 or self.__height == 0:
            return ""

        for h in range(self.__height):
            for w in range(self.__width):
                everynew_rectangle += str(self.print_symbol)
            if h is not self.__height - 1:
                everynew_rectangle = everynew_rectangle + "\n"
        return everynew_rectangle

    def __repr__(self):
        """
        repr - returns a string representation of a string

        """
        str_rep = "Rectangle({}, {})".format(self.__width, self.__height)

        return str_rep

    def __del__(self):
        """
        del - this will destroy an instance and print a message

        We also get the oppourtinity decrement, removing an instance of a rect
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
