#!/usr/bin/python3
"""Module contains function that checks parent class of an object"""


def inherits_from(obj, a_class):
    """ Checks if obj is a child of a_class.
        Returns True if it is, False if not.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
