#!/usr/bin/python3
class Square:
    """ intializing square class """
    def __init__(self, size=0, position=(0, 0)):
        """
        init allows us to create an instance
        and gave it attributes like size(set to 0). We also accounted for
        exceptions like if it was an integer or if the size was less than zero.

        Args:
        self - allows an object to refer to itself
        size - is the size of the square
        position - placement/must be a tuple of 2 positive integers

        Return:
        None

        """

        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """
        size - Size is the size of the of the square.

        Args:
        self - allows an object to refer to itself

        Return:
        Going to return the size of the size

        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        size - Size is the size of the square.

        Args:
        self - allows an object to refer to itself
        value - Value is the size we are going to set

        Return:
        None, going to set the size to the current value

        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        position - position will give the position of the square

        Args:
        self - allows an object to refer to itself

        Return:
        None

        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        position - position will give the position of the square

        Args:
        self - allows an object to reger to itself
        value - This is the value that we are setting

        Return:
        None
        """
        if (len(value) == 2 and isinstance(value, int) and isinstance
                (value[0], int) and isinstance(value[1]. int,) and isinstance
                (value, tuple) and value[0] >= 0 and value[1] >= 0 is false):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
            """ initializing func to return square area by multiplying """
            return self.__size * self.__size

    def my_print(self):
        """ prints in the standard output of square with # (: """

        zeroth, first = self.__position
        if self.__size == 0:
            print()
        else:
            for n in range(zeroth):
                print()
            for i in range(self.__size):
                print(" " * zeroth, end="")
                print("#" * self.__size)
