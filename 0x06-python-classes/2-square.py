#!/usr/bin/python3
class Square:
    """ intialzing square class """
    def __init__(self, size=0):
        """
        init allows us to create an instance
        and gave it attributes like size(set to 0). We also accounted for
        exceptions like if it was an integer or if the size was less than zero.

        Args:
        self - allows an object to refer to itself
        size - is the size of the square

        Return:
        None

        """
        self.___size = size

        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
