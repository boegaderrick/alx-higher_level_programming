#!/usr/bin/python3
"""N queens puzzle"""
import sys

if len(sys.argv) != 2:
    print('Usage: nqueens N')
    sys.exit(1)

try:
    n = int(sys.argv[1])
except ValueError:
    print('N must be a number')
    sys.exit(1)
if n < 4:
    print('N must be at least 4')
    sys.exit(1)

indices = []
columns = set()
diag1 = set()
diag2 = set()


def nqueens(x):
    """ Finds all possible safe queen positioning on an NxN
        chessboard using backtracking using backtracking
    """
    if x == n:
        print(indices)
        return
    for i in range(n):
        if i in columns or x + i in diag1 or x - i in diag2:
            continue
        columns.add(i)
        diag1.add(x + i)
        diag2.add(x - i)
        indices.append(['{:d}, {:d}'.format(x, i)])
        nqueens(x + 1)
        columns.remove(i)
        diag1.remove(x + i)
        diag2.remove(x - i)
        indices.remove(['{:d}, {:d}'.format(x, i)])


nqueens(0)
