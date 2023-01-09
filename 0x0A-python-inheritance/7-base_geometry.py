#!/usr/bin/python3
"""Module contains base geometry class"""


class BaseGeometry:
    """Base geometry class"""
    def __init__(self):
        """Method instantiates a class instance"""
        pass

    def area(self):
        """Calculates area"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Validates the value and type of <value>"""
        if type(value) is not int:
            raise TypeError(f'{name} must be an integer')
        if value < 1:
            raise ValueError(f'{name} must be greater than 0')
