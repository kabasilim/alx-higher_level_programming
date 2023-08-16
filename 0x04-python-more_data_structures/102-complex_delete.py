#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    dict_copy = a_dictionary.copy()
    for x, y in dict_copy.items():
        if value == y:
            a_dictionary.pop(x)
    return a_dictionary
