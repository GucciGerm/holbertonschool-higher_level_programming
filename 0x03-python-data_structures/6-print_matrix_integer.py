#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print('')
    for n in range(len(matrix)):
        for w in range(len(matrix[n])):
            if w == len(matrix[n]) - 1:  # w/o -1 it would just print 1 line
                print("{:d}".format(matrix[n][w]))
            else:  # w/o end it would print vertically
                print("{:d}".format(matrix[n][w]), end=' ')
