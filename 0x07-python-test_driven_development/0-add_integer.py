#!/usr/bin/python3
"""
add integer module
returns the sum of a and b

"""


def add_integer(a, b=98):
    """Returns the addition of a and b

    Args:
    a(int or float) - first number
    b(int or float) - second number, optional, defaults to 98

    Raises:
    TypeError('a and b must be integer')

    Returns:
    sum(int) of a and b

    """
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    elif not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')
    else:
        return int(a) + int(b)
