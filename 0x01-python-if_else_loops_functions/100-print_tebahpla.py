#!/usr/bin/python3
for i in reversed(range(ord('a'), ord('z') + 1)):
    print('{:c}'.format(i - 32 if chr(i) in "acegikmoqsuwy" else i), end='')
