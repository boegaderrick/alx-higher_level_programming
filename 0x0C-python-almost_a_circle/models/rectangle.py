#!/usr/bin/python3
"""Rectangle class module"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class definition"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Object instantiation"""
        attr_dict = {'width': width, 'height': height, 'x': x, 'y': y}
        for attr, value in attr_dict.items():
            self.validate_attr(attr, value)
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def to_dictionary(self):
        """Returns dictionary containing attribute/value pairs"""
        dictionary = {
                'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width
                }
        return dictionary

    def __setattr__(self, attr, value):
        """Validates value passed to setattr function before assignment"""
        self.validate_attr(attr, value)
        super().__setattr__(attr, value)

    def update(self, *args, **kwargs):
        """Updates attributes by order using *args/**kwargs"""
        if len(args) < 1:
            for attr, val in kwargs.items():
                setattr(self, attr, val)
        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass

    def __str__(self):
        """Formats object as string and returns resulting string"""
        w = self.__width
        h = self.__height
        x = self.__x
        y = self.__y
        return f'[{type(self).__name__}] ({self.id}) {x}/{y} - {w}/{h}'

    def display(self):
        """Method prints rectangle to stdout using specified char"""
        w = self.__width
        h = self.__height
        x = self.__x
        y = self.__y
        for i in range(y):
            print()
        for i in range(h):
            print('{:>{}}'.format('', x), end='')
            for j in range(w):
                print('#', end='')
            print()

    def area(self):
        """Method calculates and returns the area of a rectangle instance"""
        return self.__width * self.__height

    def validate_attr(self, attr, value):
        """Validates all passed attribute values"""
        if attr == 'size':
            attr = 'width'
        if type(value) is not int:
            raise TypeError(f'{attr} must be an integer')
        if (attr == 'x' or attr == 'y') and value < 0:
            raise ValueError(f'{attr} must be >= 0')
        elif (attr == 'width' or attr == 'height') and value < 1:
            raise ValueError(f'{attr} must be > 0')

    @property
    def width(self):
        """Getter method for width instance attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method for width instance attribute"""
        self.validate_attr('width', value)
        self.__width = value

    @property
    def height(self):
        """Height instance attribute getter method"""
        return self.__height

    @height.setter
    def height(self, value):
        """Height instance attribute setter method"""
        self.validate_attr('height', value)
        self.__height = value

    @property
    def x(self):
        """Getter method for x instance attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter method for x instance attribute"""
        self.validate_attr('x', value)
        self.__x = value

    @property
    def y(self):
        """Y attribute getter method"""
        return self.__y

    @y.setter
    def y(self, value):
        """Y attribute setter method"""
        self.validate_attr('y', value)
        self.__y = value
