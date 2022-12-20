#!/usr/bin/python3
"""square class"""


class Square:
    """initializes Square object"""
    def __init__(self, size=0, position=(0, 0)):
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")
        valid = True
        if len(position) != 2:
            valid = False
        for i in position:
            if not isinstance(i, int) or i < 0:
                valid = False
        if not valid:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = position

    """returns area of square"""
    def area(self):
        return self.__size**2

    """returns value of self.__size"""
    @property
    def size(self):
        return self.__size

    """modifies/sets value of self.__size"""
    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    """prints/draws square with '#' char in stdout"""
    def my_print(self):
        if self.__size:
            p = self.__position
            s = self.__size
            for i in range(p[1]):
                print()
            for j in range(s):
                for k in range(p[0]):
                    print(' ', end='')
                for y in range(s):
                    print('#', end='')
                print()
        else:
            print()

    """returns position attribute of object"""
    @property
    def position(self):
        return self.__position

    """sets position attribute"""
    @position.setter
    def position(self, position=()):
        valid = True
        if len(position) != 2:
            valid = False
        for i in position:
            if not isinstance(i, int) or i < 0:
                valid = False
        if not valid:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = position
