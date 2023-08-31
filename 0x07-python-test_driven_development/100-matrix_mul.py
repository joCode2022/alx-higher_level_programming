#!/usr/bin/python3
"""
Module composed by a function that multiplies 2 matrices
"""

def matrix_mul(e_f, x_y):
    """ Function that multiplies 2 matrices
    Args:
        e_f: matrix a
        x_y: matrix b
    Returns:
        result of the multiplication
    Raises:
        TypeError: if e_f or x_y aren't a list
        TypeError: if e_f or x_y aren't a list of a lists
        ValueError: if e_f or x_y are empty
        TypeError: if the lists of e_f or x_y don't have integers or floats
        TypeError: if the rows of e_f or x_y don't have the same size
        ValueError: if e_f and x_y can't be multiplied
    """

    if not isinstance(e_f, list):
        raise TypeError("e_f must be a list")

    if not isinstance(x_y, list):
        raise TypeError("x_y must be a list")

    for elems in e_f:
        if not isinstance(elems, list):
            raise TypeError("e_f must be a list of lists")

    for elems in x_y:
        if not isinstance(elems, list):
            raise TypeError("x_y must be a list of lists")

    if len(e_f) == 0 or (len(e_f) == 1 and len(e_f[0]) == 0):
        raise ValueError("e_f can't be empty")

    if len(x_y) == 0 or (len(x_y) == 1 and len(x_y[0]) == 0):
        raise ValueError("x_y can't be empty")

    for lists in e_f:
        for elems in lists:
            if not type(elems) in (int, float):
                raise TypeError("e_f should contain only integers or floats")

    for lists in x_y:
        for elems in lists:
            if not type(elems) in (int, float):
                raise TypeError("x_y should contain only integers or floats")

    length = 0

    for elems in e_f:
        if length != 0 and length != len(elems):
            raise TypeError("each row of e_f must be of the same size")
        length = len(elems)

    length = 0

    for elems in x_y:
        if length != 0 and length != len(elems):
            raise TypeError("each row of x_y must be of the same size")
        length = len(elems)

    if len(e_f[0]) != len(x_y):
        raise ValueError("e_f and x_y can't be multiplied")

    r1 = []
    i1 = 0

    for a in e_f:
        r2 = []
        i2 = 0
        num = 0
        while (i2 < len(x_y[0])):
            num += a[i1] * x_y[i1][i2]
            if i1 == len(x_y) - 1:
                i1 = 0
                i2 += 1
                r2.append(num)
                num = 0
            else:
                i1 += 1
        r1.append(r2)

    return r1
