#!/usr/bin/python3
"""Module contains function that checks type or parent class of an object"""


def is_kind_of_class(obj, a_class):
    """ Checks if obj is an instance of a_class.
        Returns True if it is, False if not.
    """
    return isinstance(obj, a_class)
