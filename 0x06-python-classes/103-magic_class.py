#!/usr/bin/python3

"""Define a MagicClass matching exactly a bytecode provided by Alx."""

import math


class MagicClass:
    """MagicClass representing a circle"""
    def __init__(self, radius=0):
        """Initialize a magicClass

        Args:
        radius(int or float)

        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """returns the area"""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """returns the circumference"""
        return (2 * math.pi * self.__radius)
