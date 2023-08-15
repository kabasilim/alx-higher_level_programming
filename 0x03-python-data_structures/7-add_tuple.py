#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len1 = len(tuple_a)
    len2 = len(tuple_b)

    a = 0 if len1 == 0 else tuple_a[0]
    b = 0 if len1 < 2 else tuple_a[1]
    c = 0 if len2 == 0 else tuple_b[0]
    d = 0 if len2 < 2 else tuple_b[1]

    tuple_c = (a + c, b + d)
    return tuple_c
