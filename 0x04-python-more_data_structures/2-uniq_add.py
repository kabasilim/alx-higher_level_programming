#!/usr/bin/python3
def uniq_add(my_list=[]):
    sorted_list = set(my_list)
    result = 0
    for i in sorted_list:
        result += i
    return result
