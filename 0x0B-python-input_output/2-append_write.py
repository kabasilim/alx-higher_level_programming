#!/usr/bin/python3
"""append write module"""


def append_write(filename="", text=""):
    """appends content to a file"""
    with open(filename, 'a', encoding="utf-8") as f:
        text = str(text)
        return f.write(text)
