#!/usr/bin/python3
"""Module that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by div.
    Args:
        matrix (list): A list of lists of integers or floats.
        div (int/float): The divisor.
    Raises:
        TypeError: If matrix is not a list of lists of ints/floats.
        TypeError: If rows of the matrix are not the same size.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is 0.
    Returns:
        A new matrix with the results of the division.
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all(len(row) > 0 for row in matrix) or
            not all(isinstance(ele, (int, float))
                    for row in matrix for ele in row)):
        raise TypeError(msg)

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [list(map(lambda x: round(x / div, 2), row)) for row in matrix]
