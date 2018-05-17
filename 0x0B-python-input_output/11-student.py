#!/usr/bin/python3
class Student:
    """
    Creating a class named Student
    """
    def __init__(self, first_name, last_name, age):
        """
        __init__ - Initializing attibutes

        Args:
        first_name - This is the first name passed
        last_name - This is the last name passed
        age - This is the age passed

        Return:
        Here we want to return the dictionary representation of student
        instances

        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        to_json - This will retrieve the dictionary representation
        of Student instance

        Return:
        The dictionary
        """
        return (self.__dict__)
