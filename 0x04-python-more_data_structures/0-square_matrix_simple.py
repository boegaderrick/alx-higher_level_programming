#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    i = 0
    for x in matrix:
        new.append([])
        for y in x:
            new[i].append(y ** 2)
        i += 1
    return new
