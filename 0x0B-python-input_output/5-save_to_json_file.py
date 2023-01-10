#!/usr/bin/python3
"""Serialization to file"""
from json import dump


def save_to_json_file(my_obj, filename):
    """Writes object as a json formatted string to file"""
    with open(filename, mode='a', encoding='utf=8') as file:
        dump(my_obj, file)
