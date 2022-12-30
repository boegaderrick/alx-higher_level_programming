#!/usr/bin/python3
"""Unittest for max_integer([...])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """subclass of the TestCase class in the unittest module"""
    def test_matching_return(self):
        """method checks whether or not function returns the correct value"""
        self.assertEqual(max_integer([2, 4, -1]), 4)
        self.assertEqual(max_integer([-9685, -9999, 0]), 0)
        self.assertEqual(max_integer([98, 58, 25*10]), 250)
        self.assertEqual(max_integer([54]), 54)
        self.assertEqual(max_integer([62, 62]), 62)

    def test_None_return(self):
        """method checks whether funtion returns None when necessary"""
        self.assertIsNone(max_integer([]))
