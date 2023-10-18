#!/usr/bin/python3
"""The Square class derived from the BaseGeometry class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """The Square Class"""
    def __init__(self, size):
        """initialization"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
