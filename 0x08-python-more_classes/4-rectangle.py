#!/usr/bin/python3
"""Rectangle class module"""


class Rectangle:
    """Rectangle class"""
    def __init__(self, width=0, height=0):
        """Method initializes class instance"""
        if type(width) is not int:
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')
        self.__width = width

        if type(height) is not int:
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be >= 0')
        self.__height = height

    """ WIDTH ATTRIBUTE MUTATORS """
    @property
    def width(self):
        """Method retrieves width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width attribute"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    """ HEIGHT ATTRIBUTE MUTATORS """
    @property
    def height(self):
        """Retrieves height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height attribute"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Calculates and returns the area of Rectangle instance"""
        return self.__height * self.__width

    def perimeter(self):
        """Calculates and returns the perimeter of Rectangle instance"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """ Returns a string of '#' and newline chars that represent
            the Rectangle instance.
        """
        rectangle = ''
        h = self.__height
        w = self.__width
        if h == 0 or w == 0:
            return rectangle
        for i in range(h):
            for j in range(w):
                rectangle += '#'
            rectangle += '\n' if i <= h - 2 else ''
        return rectangle

    def __repr__(self):
        """Returns formal string representation of Rectangle instance"""
        return 'Rectangle({:d}, {:d})'.format(self.__width, self.__height)
