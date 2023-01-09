#!/usr/bin/python3
"""Module contains function that modifies an object"""


def add_attribute(obj, attr, value):
    """Adds an attribute to an object, raises exception if operation failed"""
    imms = [int, float, complex, bool, str, bytes, tuple, frozenset]
    for i in imms:
        if type(obj) is i or isinstance(obj, i):
            raise TypeError('can\'t add new attribute')
    setattr(obj, attr, value)
