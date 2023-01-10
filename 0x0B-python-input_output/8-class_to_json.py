#!/usr/bin/python3
"""Cjlass to json function"""


def class_to_json(obj):
    """Returns dictionary attribute of an object"""
    return obj.__dict__
