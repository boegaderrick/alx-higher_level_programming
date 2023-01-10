#!/usr/bin/python3
"""Serialization module"""
from json import dumps


def to_json_string(my_obj):
    """Serializes python object to json formatted string"""
    return dumps(my_obj)
