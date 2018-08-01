#!/usr/bin/python3
"""
This script will be containing a function that finds the peak w/ unsorted list
"""


def find_peak(list_of_integers):
    """
    find_peak - This function will find the peak in a list of unsorted
    integers

    list_of_integers - An unsorted list of integers
    """

    if list_of_integers is None or len(list_of_integers) == 0:
        return None

    mid = len(list_of_integers) / 2
    mid = int(mid)

    try:
        if list_of_integers[mid - 1] <= list_of_integers[mid] and \
           list_of_integers[mid + 1] <= list_of_integers[mid]:
            return (list_of_integers[mid])

    except BaseException:
        if list_of_integers[mid - 1] < list_of_integers[mid]:
            return (list_of_integers[mid])

    if list_of_integers[mid - 1] > list_of_integers[mid]:
        return (find_peak(list_of_integers[:mid]))

    else:
        return (find_peak(list_of_integers[mid:]))
