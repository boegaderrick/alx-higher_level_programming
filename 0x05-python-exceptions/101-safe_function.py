#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        result = fct(args[0], args[1])
    except Exception as e:
        result = None
        print("Exception: " + str(e), file=sys.stderr)
    return result
