#!/usr/bin/python3
"""read file module"""


def read_file(filename=""):
    """Reads a file and prints to standard output"""
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            print(line, end='')
        # read_data = f.read()
        # print(read_data, end='')
