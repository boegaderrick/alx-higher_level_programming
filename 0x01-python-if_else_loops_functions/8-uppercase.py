#!/usr/bin/python3
def uppercase(str):
    lower = "abcdefghijklmnopqrstuvwxyz"
    for l in str:
        print('{:c}'.format(ord(l) - 32 if l in lower else ord(l)), end='')
    print(''.format())
