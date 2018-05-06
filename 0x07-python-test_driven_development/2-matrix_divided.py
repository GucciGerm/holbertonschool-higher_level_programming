#!/usr/bin/python3
"""
matrix division module
"""


def matrix_divided(matrix, div):

    """
    matrix_divided - This is going to divide all elements of a matrix

    Args:
    matrix - Complex lines of arrays intersecting, rectangular array of numbers

    Return:
    You will need to return the new matrix
    """
    if type(matrix) != int and type(matrix) != float:
        raise TypeError("matrix must be a matrix (list of lists)
of integers/floats")
    if matrix is none:
        raise TypeError("matrix must be a matrix (list of lists)
of integers/floats")
    if type(matrix) == str and type(matrix) == tuple:
        raise TypeError("matrix must be a matrix (list of lists)
of integers/floats")
    if div is 0:
        raise ZeroDivisionError("division by zero")

    create_matrix = []
    for row in range(len(matrix)):
         create_matrix.append([])
         for element in matrix[row]:
             create_matrix[row].append(round((element/div), 2))
    return create_matrix

if __name__ == "__main__":
    import doctest
    doctest.testfile("/test/2-matrix_divided.txt")
