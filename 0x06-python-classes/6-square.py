#!/usr/bin/python3

"""
This module defines a Square class

"""


class Square:

    """Square class

        Attributes:
        size (int): size of the square
        position (int, int): The position of the new square
    """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        """gets the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the size of the square"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """gets the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) != tuple or len(value) != 2 or\
                not all(isinstance(val, int) for val in value) or\
                not all(val >= 0 for val in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """area: returns the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """my_print: prints in stdout the square with the character #"""
        if self.__size == 0:
            print("")
        else:
            for x in range(self.__position[1]):
                print("")
            for y in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
