#!/usr/bin/python3
"""
    This script fetches the status of a site
    The content of the response body is printed in custom format
"""
from urllib.request import urlopen
with urlopen('https://alx-intranet.hbtn.io/status') as response:
    content = response.read()
    print('Body response:')
    print(f'\t- type: {type(content)}')
    print(f'\t- content: {content}')
    print(f'\t- utf8 content: {content.decode()}')
