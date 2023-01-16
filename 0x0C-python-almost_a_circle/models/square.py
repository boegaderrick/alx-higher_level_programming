#!/usr/bin/python3
"""Square class module"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class definition"""
    def __init__(self, size, x=0, y=0, id=None):
        """Class instance instantiation"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns string representation of object"""
        name = type(self).__name__
        return f'[{name}] ({self.id}) {self.x}/{self.y} - {self.width}'

    def update(self, *args, **kwargs):
        """Updates attributes of square object"""
        if len(args) < 1:
            for attr, value in kwargs.items():
                setattr(self, attr, value)
        else:
            attrs = ['id', 'size', 'x', 'y']
            for attr, value in zip(attrs, args):
                setattr(self, attr, value)

    def to_dictionary(self):
        """Returns dictionary containing attribute/value pairs"""
        d = {'id': self.id, 'x': self.x, 'size': self.width, 'y': self.y}
        return d

    @property
    def size(self):
        """Returns width of square object"""
        return self.width

    @size.setter
    def size(self, value):
        """Sets square width and height attributes"""
        self.width = value
        self.height = value
