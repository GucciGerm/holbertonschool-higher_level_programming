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

    def to_json(self, attrs=None):
        """
        to_json - This will retrieve the dictionary representation
        of Student instance

        Args:
        attrs - These are the attibutes

        """
        if attrs is None:
            return (self.__dict__)
        else:
            dictionary = {}
            for index, val in self.__dict__.items():
                if index in attrs:
                    dictionary[index] = val
            return dictionary

    def reload_from_json(self, json):
        """
        reload_from_json - This function will replace all attributes
        of the Student instance

        Args:
        json - This is what we'll be swapping in

        Return:
        None just return the replaced attributes
        """

        
