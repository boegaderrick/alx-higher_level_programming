#!/usr/bin/python3
""" module contains a function that takes in an int argument
    and prints a square with the int as its dimensions
"""


def print_square(size):
    """ prints to stdout a square of area 'size*size'
        using '#' characters
    """
    if type(size) is not int:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for i in range(size):
        for j in range(size):
            print('#', end='')
        print()
