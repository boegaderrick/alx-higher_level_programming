#!/usr/bin/python3
"""Module contains definition of Student class"""


class Student:
    """Student class"""
    def __init__(self, first_name, last_name, age):
        """Student class object instantiation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Returns object __dict__ if attrs is None. If attrs is list
            of strings, only attributes specified in attrs are returned
        """
        if type(attrs) is list and all(isinstance(x, str) for x in attrs):
            return {i: j for i, j in self.__dict__.items() if i in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """Modifies obj attributes specified by the key value pairs of json"""
        for i, j in json.items():
            self.__dict__[i] = j
