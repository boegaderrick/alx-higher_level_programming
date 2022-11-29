#!/usr/bin/python3
for i in range(ord('a'), ord('z') + 1):
    if i in [ord('q'), ord('e')]:
        continue
    print('{:c}'.format(i), end='')
