#!/usr/bin/python3
"""
    This script sends a request to a url by means of the requests package
    The resulting status code is printed if greater than or equal to 400
    Else the resulting text body is printed
"""
if __name__ == '__main__':
    from requests import get
    from sys import argv
    foo = get(argv[1])
    code = foo.status_code
    print(f'Error code: {code}' if code >= 400 else foo.text)
