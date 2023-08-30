#!/usr/bin/python3

"""
This module defines a Square class

"""


class Square:

    """Square class

        Attributes:
        attr1(size): size of the square
    """
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """area: returns the area of the square"""
        return self.__size ** 2
