#!/usr/bin/python3
"""
    This script sends a request to a url by means of the requests package
"""
if __name__ == '__main__':
    from requests import get
    foo = get('https://alx-intranet.hbtn.io/status')
    print('Body response:')
    print(f'\t- type: {type(foo.text)}')
    print(f'\t- content: {foo.text}')
