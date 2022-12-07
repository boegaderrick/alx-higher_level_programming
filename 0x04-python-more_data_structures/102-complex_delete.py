#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    dels = []
    for x in a_dictionary:
        if a_dictionary[x] == value:
            dels.append(x)
    for i in dels:
        del a_dictionary[i]
    return a_dictionary
