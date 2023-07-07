#!/usr/bin/python3
"""Defines a matrix multiplication function using NumPy"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiplies two matrices using NumPy"""

    return np.matmul(m_a, m_b)
