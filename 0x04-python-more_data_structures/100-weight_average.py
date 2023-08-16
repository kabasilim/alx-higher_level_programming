#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    weight_sum = sum([j for (i, j) in my_list])
    product_sum = sum([i * j for (i, j) in my_list])
    return product_sum / weight_sum
