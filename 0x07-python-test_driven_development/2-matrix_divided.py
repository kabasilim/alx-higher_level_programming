#!/usr/bin/python3
"""
matrix divided module
Divides all the elements of a matrix
Returns a new matrix
"""


def matrix_divided(matrix, div):
    """ Divides all the elements of a matrix

    Args:
    matrix (2-dimensional array)
    div (int)

    Raises:
    TypeError: if matrix is not a list of lists with integer or float
    TypeError: if each row of the matrix doesn't have the same length
    TypeError: if div is not an onteger or float
    ZeroDivisionError: if div is zero
    Returns a new matrix

    """
    new_matrix = []

    if not isinstance(matrix, list) or\
            not all(isinstance(row, list) for row in matrix) or\
            not all(isinstance(y, (int, float)) for row in
                    matrix for y in row):
        raise TypeError(
                'matrix must be a matrix (list '
                'of lists) of integers/floats')
    elif not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    elif not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    else:
        for elem in matrix:
            new_list = []
            for num in elem:
                result = round(num / div, 2)
                new_list.append(result)
            new_matrix.append(new_list)

    # if not isinstance(div, (int, float)):
    #     raise TypeError("div must be a number")
    # elif div is 0:
    #     raise ZeroDivisionError("division by zero")
    # else:
    #     for elem in matrix:
    #         new_list = []
    #         if len(elem) != len(matrix[0]):
    #             raise TypeError("Each row of\
    #                the matrix must have the same size")
    #         else:
    #             for num in elem:
    #                 if not isinstance(num, (int, float)):
    #                     raise TypeError("matrix must be a matrix\
    #                        (list of lists) of integers/floats")
    #                 else:
    #                     result = round(num / div, 2)
    #                     new_list.append(result)
    #         new_matrix.append(new_list)
    return new_matrix
