#!/usr/bin/python3
""" Module contains function that breaks down a string and outputs
    the broken up pieces to stdout.
"""


def text_indentation(text):
    """ Function breaks down string passed as argument to smaller
        chunks and outputs the smaller pieces to stdout in individual
        lines separated by blank lines.
        The chars ['.', '?', ':'] are used as delimiters marking
        end of a string and beginning of another. White spaces between
        delimiters and next string, beginning and end of str arg are ignored.
    """
    i = 0
    if type(text) is not str:
        raise TypeError('text must be a string')
    while i < len(text):
        if i > 0 and text[i - 1] in ['.', '?', ':']:
            print('\n')
            while i < len(text) and text[i] == ' ':
                i += 1
        if i == 0 and text[i] == ' ':
            while i < len(text) and text[i] == ' ':
                i += 1

        j = i
        while j < len(text) - 1 and text[j] == ' ' and text[j + 1] == ' ':
            j += 1
            if j == len(text) - 1 and text[j] == ' ':
                i = j

        if i == (len(text) - 1) and text[i] == ' ':
            i += 1
            continue
        if i < len(text):
            print(text[i], end='')
        i += 1
