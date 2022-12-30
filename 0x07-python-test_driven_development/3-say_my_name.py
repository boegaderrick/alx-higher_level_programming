#!/usr/bin/python3
"""module contains a function that prints the user's name"""


def say_my_name(first_name, last_name=""):
    """function takes in two string arguments and prints to stdout"""
    args = {first_name: 'first_name', last_name: 'last_name'}
    for i in args:
        if type(i) is not str:
            raise TypeError(args[i] + ' must be a string')
    if len(first_name) < 1 and len(last_name) < 1:
        raise ValueError('at least one name must be of valid length (>0)')
    print('My name is {:s} {:s}'.format(first_name, last_name))
