#!/usr/bin/python3
# 101-lazy_matrix_mul.py
"""Defines a matrix multiplication function using NumPy."""
import numpy as np

def lazy_matrix_mul(n_a, n_b):
    """Return the multiplication of two matrices.
    Args:
        n_a (list of lists of ints/floats): The first matrix.
        n_b (list of lists of ints/floats): The second matrix.
    """

    return (np.matmul(n_a, n_b))
