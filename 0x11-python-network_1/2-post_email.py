#!/usr/bin/python3
"""
    This script posts data to a url
"""
if __name__ == '__main__':
    from urllib.request import urlopen, Request
    import sys
    url = sys.argv[1]
    data = f'email={sys.argv[2]}'.replace('@', '%40')
    data = data.encode('ascii')
    req = Request(url, data)
    with urlopen(req) as response:
        print(response.read().decode('utf-8'))
