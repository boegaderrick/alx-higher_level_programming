#!/usr/bin/python3
"""Module contains base geometry class"""


class BaseGeometry:
    """Base geometry class"""
    def __init__(self):
        pass

    """Calculates area"""
    def area(self):
        raise Exception('area() is not implemented')
