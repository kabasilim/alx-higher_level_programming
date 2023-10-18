#!/usr/bin/python3
"""
The Rectangle class
"""


class Rectangle:
    """A rectangle class"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """gets the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width of the rectangle"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """gets the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height of the rectangle"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.__height is 0 or self.__width is 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

    def __str__(self):
        """returns a string that represents the rectangle with '#' """
        rec_string = ''
        if self.__width is 0 or self.__height is 0:
            return rec_string
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    rec_string += '#'
                if i is not self.height - 1:
                    rec_string += '\n'
        return rec_string

    def __repr__(self):
        """returns a string representation of the rectangle """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
