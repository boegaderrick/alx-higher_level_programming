#!/usr/bin/python3
def pow(a, b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    else:
        result = a
        if b < 0:
            for i in range(abs(b)):
                result *= a
            result = a / result
        else:
            for i in range(1, b):
                result *= a
    return result
