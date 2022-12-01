#!/usr/bin/python3
if __name__ == '__main__':
    import sys
argv = sys.argv
argc = len(argv)
if argc < 2:
    print('{:d} arguments.'.format(argc - 1))
elif argc == 2:
    print('{:d} argument:'.format(argc - 1))
else:
    print('{:d} arguments:'.format(argc - 1))
for i in range(argc):
    if i < 1:
        continue
    print('{:d}: {:s}'.format(i, argv[i]))
