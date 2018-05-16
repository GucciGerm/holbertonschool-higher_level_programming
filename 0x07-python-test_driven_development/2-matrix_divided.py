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
    MatrixError = "matrix must be a matrix (list of lists) of integers/floats"

    if type(matrix) != int and type(matrix) != float:
        raise TypeError(MatrixError)
    if matrix is none:
        raise TypeError(MatrixError)
    if type(matrix) == str:
        raise TypeError(MatrixError)
    if type(matrix) == tuple:
        raise TypeError(MatrixError)
    if div is 0:
        raise ZeroDivisionError("division by zero")

    for rows in matrix:
        for elements in rows:
            if not isinstance(elements, (int, float)):
                raise TypeError(MatrixError)

    new_matrix = []
    for rows in matrix:
         if not isinstance(div, (int, float)):
             raise TypeError("div must be a number")
         else:
             new_matrix.append([round((element / div), 2) for element in rows])
    return new_matrix

if __name__ == "__main__":
    import doctest
    doctest.testfile("/test/2-matrix_divided.txt")
