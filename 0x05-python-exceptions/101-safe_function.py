#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        result = fct(args[0], args[1])
    except ValueError as v:
        result = None
        print("Exception: " + str(v), file=sys.stderr)
    except TypeError as t:
        result = None
        print("Exception: " + str(t), file=sys.stderr)
    except ZeroDivisionError as z:
        result = None
        print("Exception: " + str(z), file=sys.stderr)
    except IndexError as i:
        result = None
        print("Exception: " + str(i), file=sys.stderr)
    except NameError as n:
        result = None
        print("Exception: " + str(n), file=sys.stderr)

    return result
