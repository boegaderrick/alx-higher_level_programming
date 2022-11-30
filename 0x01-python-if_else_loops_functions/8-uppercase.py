#!/usr/bin/python3
def uppercase(str):
    lower = "abcdefghijklmnopqrstuvwxyz"
    for letter in str:
        if letter in lower:
            print('{:c}'.format(ord(letter) - 32), end='')
        else:
            print('{:c}'.format(ord(letter)), end='')
    print()
