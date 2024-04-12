#!/usr/bin/python3
def matrix_divided(matrix, div):
    """Divides all elements of a matrix.

    Args:
        matrix: A list of lists of integers or floats.
        div: The divisor (integer or float).

    Raises:
        TypeError: If the matrix is not a list of lists of integers/floats,
                   if rows have different sizes, or if div is not a number.
        ZeroDivisionError: If div is 0.

    Returns:
        A new matrix with all elements divided by div.
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not all(isinstance(element, (int, float)) for row in matrix for element in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    return [[round(element / div, 2) for element in row] for row in matrix]
