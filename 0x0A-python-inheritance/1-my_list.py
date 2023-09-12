#!/usr/bin/python3
"""My list class"""


class MyList(list):
    """MyList class - a subclass of the list object"""

    def print_sorted(self):
        """Prints a sorted list"""
        print(sorted(self))
