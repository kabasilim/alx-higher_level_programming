#!/usr/bin/python3
"""Look up module
"""


def lookup(obj):
    """returns the list of available attributes and methods of an object

        Args:
        obj - object

        Returns: list object of attributes and methods of obj
    """

    return dir(obj)
