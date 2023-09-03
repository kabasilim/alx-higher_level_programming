#!/usr/bin/python3
"""
text_indentation module
prints two new lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """prints two new lines after each of these characters: ., ? and :

    Args:
    text(string)
    """

    if type(text) is not str:
        raise TypeError("text must be a string")
    else:
        i = 0
        for char in '.:?':
            text = text.replace(char, '{}\n\n'.format(char))
            lines = text.splitlines(True)
        while i < len(lines) - 1:
            print(lines[i].strip())
            i += 1
        if lines[i][len(lines[i]) - 1] == '\n':
            print(lines[i].strip())
        else:
            print(lines[i].strip(), end='')
