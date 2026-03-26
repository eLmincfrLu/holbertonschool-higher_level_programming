#!/usr/bin/python3
"""Module that divides all elements of a matrix"""
def matrix_divided(matrix, div):
    """Divide all elements of a matrix by div, raise TypeError/ZeroDivisionError if invalid."""
    if (not isinstance(matrix, list) or 
        not all(isinstance(row, list) for row in matrix) or
        not all(isinstance(element, (int, float)) for row in matrix for element in row)
    ):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    lenn = []
    for row in matrix:
        lenn.append(len(row))
    if sum(lenn) != lenn[0] * len(lenn):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_list = [list(map(lambda x: round((x / div), 2), row)) for row in matrix]
    return new_list
