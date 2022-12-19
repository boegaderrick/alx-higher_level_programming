#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    argv = []
    try:
        for a in range(2):
            try:
                argv.append(args[a])
            except IndexError as i:
                print("Exception: " + str(i), file=sys.stderr)
                return None
        result = fct(argv[0], argv[1])
    except Exception as e:
        result = None
        print("Exception: " + str(e), file=sys.stderr)
    return result
