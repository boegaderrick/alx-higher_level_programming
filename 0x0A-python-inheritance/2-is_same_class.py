#!/usr/bin/python3
"""Module contains function that checks type of object"""


def is_same_class(obj, a_class):
    """ Checks the type of obj.
        Returns True if it matches a_class, false if not
    """
    if type(obj) is a_class:
        return True
    return False
