#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    empty = []
    for n in matrix:
        empty.append(list(map(lambda n: n**2, n)))
    return empty
