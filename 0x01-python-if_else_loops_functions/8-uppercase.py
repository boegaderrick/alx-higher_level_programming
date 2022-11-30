#!/usr/bin/python3
def uppercase(str):
    lower = "abcdefghijklmnopqrstuvwxyz"
    for lt in str:
        print('{:c}'.format(ord(lt) - 32 if lt in lower else ord(lt)), end='')
    print(''.format())
