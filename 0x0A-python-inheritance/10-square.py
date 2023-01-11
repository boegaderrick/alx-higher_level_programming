#!/usr/bin/python3
"""Module contains classes that are connected by inheritance"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class derived from Rectangle and BaseGeometry classes"""
    def __init__(self, size):
        super(Rectangle, self).integer_validator("size", size)
        super().__init__(size, size)
