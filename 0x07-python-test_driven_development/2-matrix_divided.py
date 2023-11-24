#!/usr/bin/python3

""" This is the 2-matrix_divided module
    it's provide a function to perform the division
    of all the elements of a matrix
"""


def matrix_divided(matrix, div):
    """Divide the element of a matrix
    Args:
        matrix(list of lists): a mtrix of elements
        div(integer or float): the number we use to divide
                        the elements of the matrix
    """

    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list) or len(matrix) == 0 or not matrix[0]:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    for row in matrix:
        if len(row) == 0:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")

    for i in row:
        if type(i) not in (int, float):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")

    len_row = []
    for row in matrix:
        len_row.append(len(row))
    if not all(elem == len_row[0] for elem in len_row):
        raise TypeError("Each row of the matrix must have the same size")

    return ([[round(i / div, 2) for i in row] for row in matrix])
