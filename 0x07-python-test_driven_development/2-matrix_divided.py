#!/usr/bin/python3
"""Module for matrix_divided method"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix"""

    m = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list):
        raise TypeError()
    if len(matrix) == 0:
        raise TypeError(m)
    if not isinstance(matrix[0], list):
        raise TypeError(m)
    if len(matrix[0]) == 0:
        raise TypeError(m)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise TypeError("division by zero")
    if not all(isinstance(i, (int, float)) for i in matrix[0]):
        raise TypeError(m)
    if not all(len(i) == len(matrix[0]) for i in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    return [[round(i / div, 2) for i in row] for row in matrix]
