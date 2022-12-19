#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    val = True
    try:
        print("{:d}".format(value))
    except TypeError as t:
        val = False
        print("Exception: " + str(t), file=sys.stderr)
    except ValueError as v:
        val = False
        print("Exception: " + str(v), file=sys.stderr)
    return val
