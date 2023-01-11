#!/usr/bin/python3
"""Module contains base geometry class"""


class BaseGeometry:
    """Base geometry class"""
    def __init__(self):
        """Object instatiation"""
        pass

    def area(self):
        """Calculates area"""
        raise Exception('area() is not implemented')
