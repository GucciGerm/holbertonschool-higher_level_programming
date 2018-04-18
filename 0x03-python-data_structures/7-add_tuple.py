#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) == 0:
        tupleone = 0, 0
    elif len(tuple_a) == 1:
        tupleone = tuple_a[0], 0
    else:
        tupleone = tuple_a[0], tuple_a[1]
    if len(tuple_b) == 0:
        tupletwo = 0, 0
    elif len(tuple_b) == 1:
        tupletwo = tuple_b[0], 0
    else:
        tupletwo = tuple_b[0], tuple_b[1]
    sum = tupleone[0] + tupletwo[0], tupleone[1] + tupletwo[1]
    return sum
