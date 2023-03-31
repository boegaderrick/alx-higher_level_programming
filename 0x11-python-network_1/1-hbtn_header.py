#!/usr/bin/python3
"""This script fetches a url and prints a header value"""
from urllib.request import urlopen
import sys
with urlopen(sys.argv[1]) as response:
    print(response.info().get('X-Request-Id'))
