#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    my_list = []
    for i in range(2):
        if i < len(tuple_a):
            a = tuple_a[i]
        else:
            a = 0
        if i < len(tuple_b):
            b = tuple_b[i]
        else:
            b = 0
        my_list += [a + b]
    my_tuple = my_list[0], my_list[1]
    return my_tuple
