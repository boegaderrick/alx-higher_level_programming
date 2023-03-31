#!/usr/bin/python3
"""
    This script sends a post request to a url and prints the returned
    values in custom format.
    If the values returned are not in valid json format or empty
    they are handled accordingly.
"""
if __name__ == '__main__':
    from requests import post
    from sys import argv
    from json import loads
    url = 'http://0.0.0.0:5000/search_user'
    value = '' if len(argv) < 2 else argv[1]
    foo = post(url, {'q': value})
    try:
        bar = loads(foo.text.strip())
        if len(bar) < 1:
            print('No result')
        else:
            print(f"[{bar.get('id')}] {bar.get('name')}")
    except Exception:
        print('Not a valid JSON')
