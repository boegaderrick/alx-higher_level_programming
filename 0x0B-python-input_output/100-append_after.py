#!/usr/bin/pytho3
"""Search and update"""


def append_after(filename='', search_string='', new_string=''):
    """Reads a file and inserts string in next line of keyword appearance"""
    with open(filename, mode='r', encoding='utf-8') as file:
        content = file.readlines()
    with open(filename, mode='w', encoding='utf-8') as file:
        new = ''
        for i in content:
            if search_string in i:
                new += i
                new += new_string
            else:
                new += i
        file.write(new)
