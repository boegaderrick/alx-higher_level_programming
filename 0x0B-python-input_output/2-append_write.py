#!/usr/bin/python3
"""Append write module"""


def append_write(filename='', text=''):
    """Writes/appends to file"""
    with open(filename, mode='a', encoding='utf-8') as file:
        file.write(text)
    return len(text)
