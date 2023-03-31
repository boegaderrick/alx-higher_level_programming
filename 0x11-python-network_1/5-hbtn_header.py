#!/usr/bin/python3
"""
    This script sends a request to a url by means of the requests package
    The value of 'X-Request-Id' is printed to stdout
"""
if __name__ == '__main__':
    from requests import get
    from sys import argv
    foo = get(argv[1])
    print(foo.headers.get('X-Request-Id'))
