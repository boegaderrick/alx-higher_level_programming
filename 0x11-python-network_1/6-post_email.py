#!/usr/bin/python3
"""
    This script sends a post request to a url by means of the requests package
    The resulting body is then printed to stdout
"""
if __name__ == '__main__':
    from requests import post
    from sys import argv
    foo = post(argv[1], {'email': argv[2]})
    print(foo.text)
