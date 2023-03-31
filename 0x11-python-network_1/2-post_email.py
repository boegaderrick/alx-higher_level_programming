#!/usr/bin/python3
"""
    This script posts data to a url and sends a get request
    The response of the request is printed to stdout
"""
if __name__ == '__main__':
    from urllib.request import urlopen, Request
    from urllib.parse import urlencode
    import sys
    url = sys.argv[1]
    """data = f'email={sys.argv[2]}'.replace('@', '%40')"""
    data = urlencode({'email': sys.argv[2]}).encode()
    req = Request(url, data)
    with urlopen(req) as response:
        print(response.read().decode())
