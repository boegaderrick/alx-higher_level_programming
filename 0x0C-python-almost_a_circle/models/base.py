#!/usr/bin/python3
"""Base class module"""

import json


class Base:
    """Base class definition"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Class instance constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @classmethod
    def load_from_file(cls):
        """Creates objects from json strings stored in files"""
        name = cls.__name__ + '.json'
        try:
            with open(name, mode='r', encoding='utf=8') as file:
                obj_dicts = cls.from_json_string(file.read())
        except FileNotFoundError:
            return []

        objects = []
        for i in obj_dicts:
            objects.append(cls.create(**i))
        return objects

    @staticmethod
    def from_json_string(json_string):
        """Json string deserialization"""
        if json_string is None or len(json_string) < 1:
            return []
        return json.loads(json_string)

    @staticmethod
    def to_json_string(list_dictionaries):
        """Object serialization method"""
        if list_dictionaries is None or len(list_dictionaries) < 1:
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Serialization to file"""
        list_dict = []
        if list_objs is not None:
            for i in list_objs:
                list_dict.append(cls.to_dictionary(i))
        json_string = Base.to_json_string(list_dict)
        name = cls.__name__ + '.json'
        with open(name, mode='w', encoding='utf-8') as file:
            file.write(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creates new instance from dictionary"""
        n = cls(3, 3)
        n.update(**dictionary)
        return n
