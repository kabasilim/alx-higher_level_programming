#!/usr/bin/python3
safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except Exception as error:
        return False
