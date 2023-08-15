#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        x = len(i) - 1
        for j in i:
            print("{:d}{}".format(j, " " if j != i[x] else ""), end="")
        print("")
