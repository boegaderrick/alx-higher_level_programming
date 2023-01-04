#!/usr/bin/python3
"""LockedClass module"""


class LockedClass:
    """ Class with no attributes, dynamic allocation allowed only
        for attribute named 'first_name'
    """
    __slots__ = ['first_name']
