#!/usr/bin/python3
"""
    This script sends a get request to the github api with basic authentication
    It takes two arguments, 'username' & 'password' for authentication
    The returned user's id is then printed to stdout
"""
if __name__ == '__main__':
    from requests import get
    from sys import argv
    url = 'https://api.github.com/user'
    foo = get(url, auth=(argv[1], argv[2]))
    print(foo.json().get('id'))
