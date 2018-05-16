#!/usr/bin/python3
class BaseGeometry:
    """
    Creating a class called BaseGeometry
    """

    def area(self):
        """
        area - This will check if area has been implemented
        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        integer_validator - This will validate the value to see if integer

        Args:
        name - (You can assume this is a string)
        value - This is what we're validating

        Return:
        None
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
