#!/usr/bin/python3
"""Deserialization from file"""
from json import load


def load_from_json_file(filename):
    """Returns an object file desirialized from json file"""
    with open(filename, encoding='utf-8') as file:
        obj = load(file)
    return obj
