#!/usr/bin/python3
"""Square class unittest module"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test case subclass"""
    def test_1__str__(self):
        """Checks string representaion of object"""
        s = Square(50, 6, 3, 989)
        self.assertEqual(s.__str__(), '[Square] (989) 6/3 50')
        s = Square(1, 1, 1)
        self.assertEqual(s.__str__(), '[Square] (1) 1/1 1')

    def test_2_raises(self):
        """Tests that exceptions are raised when necessary"""
        with self.assertRaises(ValueError):
            s = Square(-1, 5, 3, 5)
        s = Square(2, 3, 4, 5)
        with self.assertRaises(TypeError):
            s.width = 'j'
        with self.assertRaises(ValueError):
            s.x = -1
        with self.assertRaises(TypeError):
            s.y = None
