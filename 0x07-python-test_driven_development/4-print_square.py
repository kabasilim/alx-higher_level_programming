#!/usr/bin/python3
"""
print square module
prints a square with the character # of any size
"""


def print_square(size):
    """prints a square with the character # of any size

    Args:
    size(int)

    Raises:
    TypeError: if size is not an integer
    ValueError: if size is less than 0
    TypeError: if size is a float and less than 0
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    else:
        for i in range(size):
            for j in range(size):
                print("{}".format("#"), end="")
            print("")
