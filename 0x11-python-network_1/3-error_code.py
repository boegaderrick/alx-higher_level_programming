#!/usr/bin/python3
"""
    This script sends get request to passed url and prints response body
    HTTPError exceptions are handled if any
"""
if __name__ == '__main__':
    from urllib.request import urlopen
    from urllib.error import HTTPError
    from sys import argv
    try:
        with urlopen(argv[1]) as response:
            print(response.read().decode())
    except HTTPError as e:
        print(f'Error code: {e.code}')
