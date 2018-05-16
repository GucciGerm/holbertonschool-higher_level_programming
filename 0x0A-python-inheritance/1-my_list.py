#!/usr/bin/python3
class MyList(list):
    """
    MyList - Created this class to inherit components from list

    Args:
    list - This is the list that we will be inheriting from

    Return:
    None, will print the sorted inherited list
    """

    def print_sorted(self):
        """
        print_sorted - This will print the list, but sorted (ascending sort)

        Args:
        self - defining that we will just refer to itself

        Return:
        None
        """

        print(sorted(self))

        """ The function will print the list in sorted (ascending sort) """
