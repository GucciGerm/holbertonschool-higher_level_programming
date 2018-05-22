#!/usr/bin/python3
from models.base import Base


class Rectangle(Base):
    """
    class - Here we are creating a class

    Rectangle - Here we are creating a Rectangle class instance
    that will be inheriting from the Base instance

    Base - This is the class instance that we will have the Rectangle
    inherit

    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        __init__ - class constructor

        Args:
        width - This is how wide the rectangle is

        height - This is how tall the rectangle is

        x - (x-axis)
        y - (y-axis)

        id - This is the identification for the attributes (set to super)

        Applying Super() - the super function can be used to gain access to
        inherited methods – from a parent or sibling class – that has been
        overwritten in a class object
        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    """

    Below we will we using getter/setters to make sure they are private
    instances!
    """
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        Rectangle.validator("width", value)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        Rectangle.validator("height", value)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        Rectangle.validator("x", value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        Rectangle.validator("y", value)
        self.__y = value

    def area(self):
        """
        area - This funciton will return the width x height of
        our rectangle
        """
        return self.width * self.height

    def display(self):
        """
        display - This function will print the stdoutput the rectangle
        instance with the # by storing it to variable named hashtag
        """

        xaxisspace = " " * self.x
        yaxisspace = "\n" * self.y
        print(yaxisspace, end="")

        for yaxis in range(self.height):
            print(xaxisspace, end="")
            for xaxis in range(self.width):
                print("#", end="")
            print("")

    def __str__(self):
        """
        __str__ - This str method will return
        ([Rectangle] (<id>) <x> / <y> - <width> / <height>)
        """
        return ("[Rectangle] {} {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                      self.width, self.height))

    def update(self, *args, **kwargs):
        """
        update - This will assign an argument to each attribute

        Args:
        args - arguments being passed
        """

        attributes = ["id", "width", "height", "x", "y"]

        for tributes in range(len(args)):
            if args is not 0:
                setattr(self, attributes[tributes], args[tributes])

        for key in attributes:
            if key in kwargs and kwargs[key] is not None:
                setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """
        to_dictionary - Here we are creating the dictionary representation
        of our rectangle we created

        """

        rectanglevals = ["id", "width", "height", "x", "y"]
        dictionary = {}

        for key in rectanglevals:
            dictionary[key] = getattr(self, key)
        return dictionary
