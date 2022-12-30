#!/usr/bin/python3
"""
module with function that performs addition

"""


def add_integer(a, b=98):
    """ performs addition of two integers then returns result
        @a: first integer
        @b: second integer
        Return: result of operation
    """
    args = {a: 'a', b: 'b'}
    for i in args:
        if type(i) not in [int, float]:
            raise TypeError(args[i] + ' must be an integer')
    return int(a) + int(b)
