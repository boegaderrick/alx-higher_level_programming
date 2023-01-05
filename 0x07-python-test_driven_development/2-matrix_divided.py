#!/usr/bin/python3
""" module containing function that performs division on elements
    of passed matrix and returns new matrix with results of all
    division operations
"""


def matrix_divided(matrix, div):
    """ performs division on all elements of matrix
        @matrix: matrix containing elements to be divided
        @div: divisor to be used in operations
        Return: new matrix with result of all operations
    """
    type_error = 'matrix must be a matrix (list of lists) of integers/floats'
    len_error = 'Each row of the matrix must have the same size'
    div_error = 'div must be a number'

    if not isinstance(matrix, list):
        raise TypeError(type_error)
    if not all(isinstance(i, list) for i in matrix):
        raise TypeError(type_error)
    counter = 0
    for i in matrix:
        for j in i:
            if type(j) not in [int, float]:
                raise TypeError(type_error)
        if counter < 1:
            bench = len(i)
        else:
            if len(i) != bench:
                raise TypeError(len_error)
        counter += 1
    if div == float('inf') or div == -float('inf'):
        div = 10
    if type(div) not in [int, float]:
        raise TypeError(div_error)
    new = [[round(j / div, 2) for j in i] for i in matrix]
    return new
