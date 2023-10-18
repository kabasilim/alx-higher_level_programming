#!/usr/bin/python3
"""write file module"""


def write_file(filename="", text=""):
    """writes content to a file"""
    with open(filename, 'w', encoding="utf-8") as f:
        text = str(text)
        return f.write(text)
