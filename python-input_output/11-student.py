#!/usr/bin/python3
"""This module represents operations with files"""


class Student:
    """This is a Student class"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if isinstance(attrs, list):
            dict = {}
            for i in attrs:
                if isinstance(i, str) and hasattr(self, i):
                    dict[i] = getattr(self, i)
            return dict
        return self.__dict__

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
