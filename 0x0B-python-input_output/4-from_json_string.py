#!/usr/bin/python3
"""Deserialization module"""
from json import loads


def from_json_string(my_str):
    """Deserializes json formatted string"""
    return loads(my_str)
