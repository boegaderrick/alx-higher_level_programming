#!/usr/bin/python3
def best_score(a_dictionary):
    key = None
    if a_dictionary:
        best = -99999999999999999999
        for i in a_dictionary:
            if a_dictionary[i] > best:
                best = a_dictionary[i]
                key = i
    return key
