#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) < 1:
        first_char = None
    else:
        first_char = sentence[0]
    my_tuple = len(sentence), first_char
    return my_tuple
