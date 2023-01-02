#!/usr/bin/python3
"""Multiplication of matrices"""


def matrix_mul(m_a, m_b):
    """ Multiplies two matrices and returns a new matrix
        formed as a result of the operation.
    """
    validation(m_a, m_b)
    x = len(m_b[0])
    y = len(m_a[0])
    new = []
    for i in range(x):
        for j in range(x):
            new.append([])
            res = 0
            for k in range(y):
                index_error = False
                try:
                    res += m_a[j][k] * m_b[k][i]
                except IndexError:
                    index_error = True
                    continue
            if not index_error:
                new[j].append(res)
    new = [i for i in new if len(i) > 0]
    return new


def validation(m_a, m_b):
    """ Performs checks on the matrices passed by the caller
        to ensure the operation can be conducted on them.
        Exceptions are raised as and when necessary.
    """
    if type(m_a) is not list:
        raise TypeError('m_a must be a list')
    if type(m_b) is not list:
        raise TypeError('m_b must be a list')
    for i in m_a:
        if type(i) is not list:
            raise TypeError('m_a must be a list of lists')
    for i in m_b:
        if type(i) is not list:
            raise TypeError('m_b must be a list of lists')
    if len(m_a) < 1 or len(m_a[0]) < 1:
        raise ValueError('m_a can\'t be empty')
    if len(m_b) < 1 or len(m_b[0]) < 1:
        raise ValueError('m_b can\'t be empty')
    for i in m_a:
        for j in i:
            if type(j) not in [int, float]:
                raise TypeError('m_a should contain only integers or floats')
    for i in m_b:
        for j in i:
            if type(j) not in [int, float]:
                raise TypeError('m_b should contain only integers or floats')
    bench = len(m_a[0])
    for i in m_a:
        if len(i) != bench:
            raise TypeError('each row of m_a must be of the same size')
    bench = len(m_b[0])
    for i in m_b:
        if len(i) != bench:
            raise TypeError('each row of m_b must be of the same size')
    if len(m_a[0]) != len(m_b):
        raise ValueError('m_a and m_b can\'t be multiplied')
