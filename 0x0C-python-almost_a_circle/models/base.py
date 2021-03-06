#!/usr/bin/python3
"""
    base.py
"""
import json


class Base:
    """
    class - Here we are creating a class
    Base - Here we are creating a base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        __init__ - class constructor

        Args:
        id - Set to id to none, this is the instance's identification

        """

        if id is not None:
            self.id = id

        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        to_json_string - This will return the JSON string representation
        of list_dictionaries

        Args:
        list_dictionaries - This is a list of directories

        """

        if list_dictionaries is None:
            return ("[]")
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        save_to_file - This will write the json string representation
        of list_objs

        Args:
        cls - This is our class

        list_objs - This is a list of instances who inherits base
        """

        emptylist = []

        with open("{}.json".format(cls.__name__), mode="w",
                  encoding="utf-8") as n:

            if list_objs is None:
                n.write(Base.to_json_string([]))

            else:
                for instance in list_objs:
                    emptylist.append(instance.to_dictionary())
                n.write(Base.to_json_string(emptylist))

    @staticmethod
    def from_json_string(json_string):
        """
        from_json_string - This will return the list of the json
        string representation

        Args:
        json_string - is a string representing a list of dictionaries

        Return:
        We want to return a empty list if json_string is None
        if not then return the list represented by json_string
        """

        if json_string is None:
            return ([])
        else:
            return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """
        create - This will create a dummy instance of our methods

        Args:
        cls - This is our class method
        dictionary - This is our dictionary

        if the class name found ".json" account for (w, h)
        (size)

        Return:
        We want to return an instance with all attributes already set
        """

        if cls.__name__ == "Rectangle":
            n = cls(4, 4)
        if cls.__name__ == "Square":
            n = cls(4)

        n.update(**dictionary)
        return (n)

    @classmethod
    def load_from_file(cls):
        """
        load_from_file - This function will return a list of instances,
        all the types of these instances depends on cls(rect or squar)

        Return:
        We will return a list of instances
        """
        listoinstances = []
        """
        set an empty list
        """
        try:

            with open("{}.json".format(cls.__name__), mode="r",
                      encoding="utf-8") as n:
                listoinstances = cls.from_json_string(n.read())

            for element in range(len(listoinstances)):
                listoinstances[element] = cls.create(**listoinstances[element])
            return (listoinstances)
        except:
            return (listoinstances)
