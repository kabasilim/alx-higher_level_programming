#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counter = 1
    while (counter <= x):
        try:
            print("{}".format(my_list[counter - 1]), end="")
            counter += 1
        except Exception as error:
            break
    print("")
    return counter - 1
