#!/usr/bin/python3
"""Pascal triangle generator module"""


def pascal_triangle(n):
    """Generates a pascal triangle in a matrix"""

    tr = [[0 for j in range(i)] for i in range(1, n + 1)]
    for i in range(len(tr)):
        for j in range(i + 1):
            if j == 0:
                tr[i][j] = 1
            else:
                try:
                    num1 = tr[i - 1][j - 1]
                except IndexError:
                    num1 = 0
                try:
                    num2 = tr[i - 1][j]
                except IndexError:
                    num2 = 0
                tr[i][j] = num1 + num2
    return tr
