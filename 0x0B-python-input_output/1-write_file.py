#!/usr/bin/python3
"""Write file module"""


def write_file(filename='', text=''):
    """Function writes text to a file"""
    with open(filename, mode='w', encoding='utf-8') as file:
        file.write(text)
        ret = file.tell()
    return ret
