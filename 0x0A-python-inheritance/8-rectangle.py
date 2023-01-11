#!/usr/bin/python3
"""Module contains base geometry class"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class/BaseGeometry subclass"""

    def __init__(self, width, height):
        """Rectangle class object instantiation"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
