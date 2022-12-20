#!/usr/bin/python3
"""square class"""


class Square:
    """initializes Square objecti"""
    def __init__(self, size=0):
        """Square object
        Args:
            size: size of side
        Exceptions:
            ValueError: exception indicating size is not of expected value
            TypeError: exception indicating size is not of expected type
        """
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be and integer")
