#!/usr/bin/python3
"""Read_file module"""


def read_file(filename=""):
    """Reads a file and prints its contents to stdout"""
    with open(filename, encoding='utf-8') as file:
        content = file.read()
        for i in content:
            print(i, end='')
