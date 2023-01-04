#!/usr/bin/python3
"""Rectangle class module"""


class Rectangle:
    """Rectangle class"""
    number_of_instances = 0
    print_symbol = '#'

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
        Rectangle.number_of_instances += 1

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
                rectangle += str(self.print_symbol)
            rectangle += '\n' if i <= h - 2 else ''
        return rectangle

    def __repr__(self):
        """Returns formal string representation of Rectangle instance"""
        return 'Rectangle({:d}, {:d})'.format(self.__width, self.__height)

    def __del__(self):
        """Prints message to stdout when object deletion is detected"""
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Compares two instances of Rectangle and returns the
            larger one based on area.
        """
        if type(rect_1) is not Rectangle:
            raise TypeError('rect_1 must be an instance of Rectangle')
        if type(rect_2) is not Rectangle:
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() > rect_2.area():
            return rect_1
        elif rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        """Instantiates an object of Rectangle as a square"""
        new = cls(size, size)
        return new