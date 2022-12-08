#!/usr/bin/python3
def roman_to_int(roman_string):
    decimal = 0
    i = 0
    if not isinstance(roman_string, str):
        return decimal
    length = len(roman_string) if roman_string else 0
    if length < 1:
        return decimal
    num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for x in roman_string:
        if x not in list(num):
            return decimal
    while i < length:
        rom = roman_string[i]
        next_rom = roman_string[i + 1] if i < (length - 1) else roman_string[i]
        if num[rom] < num[next_rom]:
            decimal += (num[next_rom] - num[rom])
            i += 1
        else:
            decimal += num[rom]
        i += 1
    return decimal
