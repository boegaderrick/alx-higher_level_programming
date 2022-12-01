#!/usr/bin/python3
if __name__ == '__main__':
    import sys
numbers = sys.argv
argc = len(numbers)
result = 0
for i in range(argc):
    if i < 1:
        continue
    result += int(numbers[i])
print('{:d}'.format(result))
