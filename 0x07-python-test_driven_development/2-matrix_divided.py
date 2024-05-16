#!/usr/bin/python3

"""
This module defines a matrix division function.
"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix.

    Args:
        matrix (list of lists): A list of lists of integers or floats.
        div (int or float): A number to divide all elements of a matrix.

    Raises:
        TypeError: If the matrix is not a list of lists of integers or floats,
                   or if the rows of the matrix are not the same,
                   or if div is not an integer or float number.
        ZeroDivisionError: If div is zero.

    Returns:
        list of lists: A new matrix.
    """
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(x / div, 2) for x in row] for row in matrix]
