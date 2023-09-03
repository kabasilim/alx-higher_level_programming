#!/usr/bin/python3
"""
say my name module
prints first and last name
"""


def say_my_name(first_name, last_name=""):
    """Prints the first and last name

    Args:
    first_name(string)
    last_name(string) - optional

    Raises:
    TypeError: if first_name or last_name is not a string

    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")
    else:
        print("{} {} {}".format("My name is", first_name, last_name))
