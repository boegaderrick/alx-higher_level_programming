#!/usr/bin/python3
"""Module contains definition of Student class"""


class Student:
    """Student class"""
    def __init__(self, first_name, last_name, age):
        """Student class object instantiation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns object __dict__ attribute"""
        return self.__dict__
