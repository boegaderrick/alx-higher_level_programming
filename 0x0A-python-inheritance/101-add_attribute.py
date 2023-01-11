#!/usr/bin/python3
"""Module contains function that modifies an object"""


def add_attribute(obj, attr, value):
    """Adds an attribute to an object, raises exception if operation failed"""
    imms = [int, float, complex, bool, str, bytes, tuple, frozenset]
    for i in imms:
        if type(obj) is i or isinstance(obj, i) or issubclass(type(obj), i):
            raise TypeError('can\'t add new attribute')
    if len(obj.__slots__) > 0 and attr not in obj.__slots__:
        raise TypeError('can\'t add new attribute')
    setattr(obj, attr, value)
