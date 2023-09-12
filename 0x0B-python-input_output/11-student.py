#!/usr/bin/python3
"""Student Class"""


class Student:
    """Student Class"""

    def __init__(self, first_name, last_name, age):
        """initialization"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    # def to_json(self, attrs=None):
    #     """retrieves a dictionary representation of a Student instance"""
    #     if attrs is not None and all(isinstance(x, str) for x in attrs):
    #         new_dict = {}
    #         for x in attrs:
    #             for y in self.__dict__:
    #                 if x == y:
    #                     new_dict.update({y : self.__dict__[y]})
    #         return new_dict
    #     else:
    #         return self.__dict__

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of a Student instance."""
        if attrs is not None and all(isinstance(x, str) for x in attrs):
            d = {}
            for x, y in self.__dict__.items():
                if x in attrs:
                    d[x] = y
            return d
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """reload data from json"""
        for (key, value) in json.items():
            setattr(self, key, value)
