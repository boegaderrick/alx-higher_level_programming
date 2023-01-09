#!/usr/bin/python3
"""Module contains an int subclass"""


class MyInt(int):
    """A derived class of the int class"""
    def __init__(self, num):
        """Instantiation of a class instance"""
        self.__num = num

    def __ne__(self, num):
        """Inverted not equal comparison method"""
        return self.__num == num

    def __eq__(self, num):
        """Inverted equal comparison method"""
        return self.__num != num
