#!/usr/bin/python3
"""Matrix multiplication using numpy"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """ Multiplies two matrices and returns a new matrix containing
        the result of the multiplication
        Checks are run beforehand to ensure the operation is possible
    """
    validation(m_a, m_b)
    return np.matmul(m_a, m_b)


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
