#!/usr/bin/python3
"""square class"""


class Square:
    """initializes Square object"""
    def __init__(self, size=0):
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
    """returns area of square"""
    def area(self):
        return self.__size**2
