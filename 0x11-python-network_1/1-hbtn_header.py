#!/usr/bin/python3
"""This script fetches a url and prints a header value"""
import urllib.request
import sys
with urllib.request.urlopen(sys.argv[1]) as response:
    print(response.info().get('X-Request-Id'))
