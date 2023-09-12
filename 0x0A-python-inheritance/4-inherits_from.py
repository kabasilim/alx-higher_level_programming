#!/usr/bin/python3
"""inherits_from module"""


def inherits_from(obj, a_class):
    """Checks if obj is inherited from a_class"""

    return issubclass(type(obj), a_class) and type(obj) != a_class
