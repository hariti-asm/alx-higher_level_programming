#!/usr/bin/python3
"""Defines a matrix multiplication function"""


def matrix_mul(m_a, m_b):
    """Multiplies two matrices"""

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    for row in m_a:
        if not isinstance(row, list):
            raise TypeError("m_a must be a list of lists")
    for row in m_b:
        if not isinstance(row, list):
            raise TypeError("m_b must be a list of lists")

    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")

    for row in m_a:
        if len(row) == 0:
            raise ValueError("m_a can't be empty")
    for row in m_b:
        if len(row) == 0:
            raise ValueError("m_b can't be empty")

    for row in m_a:
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError("m_b should contain only integers or floats")

    for row in m_a:
        if len(row) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")
    for row in m_b:
        if len(row) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    new_matrix = [[0 for col in range(len(m_b[0]))] for row in range(len(m_a))]

    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                new_matrix[i][j] += m_a[i][k] * m_b[k][j]

    return new_matrix
