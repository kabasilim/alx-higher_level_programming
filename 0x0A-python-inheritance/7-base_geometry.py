#!/usr/bin/python3
"""Base Geometry class"""


class BaseGeometry:
    """Base Geometry Class"""
    def area(self):
        """calculates area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        else:
            pass
