#!/usr/bin/python3
"""Module contains base geometry class"""


class BaseGeometry:
    """Base geometry class"""
    def __init__(self):
        """Class instance instantiation"""
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


class Rectangle(BaseGeometry):
    """Rectangle class/BaseGeometry subclass"""

    def __init__(self, width, height):
        """Rectangle class object instantiation"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculates area"""
        try:
            return self.__width * self.__height
        except Exception:
            super().area()

    def __str__(self):
        """Returns a string implementation of the object fields"""
        return f'[{type(self).__name__}] {self.__width}/{self.__height}'
