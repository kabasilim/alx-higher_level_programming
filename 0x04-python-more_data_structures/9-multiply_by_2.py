#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = {}
    for item in a_dictionary:
        new_dictionary[item] = a_dictionary[item] * 2
    return new_dictionary
