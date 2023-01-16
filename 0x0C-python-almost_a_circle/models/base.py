#!/usr/bin/python3
"""Base class module"""

import json
import csv


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

    @classmethod
    def create(cls, **dictionary):
        """Creates new instance from dictionary"""
        if cls.__name__ == 'Square':
            n = cls(3)
        else:
            n = cls(3, 3)
        n.update(**dictionary)
        return n

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Writes to csv file"""
        name = cls.__name__ + '.csv'
        with open(name, mode='w', encoding='utf=8') as file:
            if list_objs is None or len(list_objs) < 1:
                csv_writer.write('[]')
                return
            if cls.__name__ == 'Square':
                fields = ['id', 'size', 'x', 'y']
            elif cls.__name__ == 'Rectangle':
                fields = ['id', 'width', 'height', 'x', 'y']
            csv_writer = csv.DictWriter(file, fieldnames=fields)
            csv_writer.writeheader()
            for i in list_objs:
                csv_writer.writerow(i.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Reads from a csv file"""
        try:
            name = cls.__name__ + '.csv'
            with open(name, mode='r', encoding='utf=8') as file:
                csv_reader = csv.DictReader(file)
                lst = []
                for i in csv_reader:
                    for j in i:
                        i[j] = int(i[j])
                    lst.append(cls.create(**dict(i)))
        except FileNotFoundError:
            lst = []
        return lst
