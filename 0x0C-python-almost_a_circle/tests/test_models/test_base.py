#!/usr/bin/python3
"""Base class unittests"""
import unittest
from models.base import Base


class TestModels(unittest.TestCase):
    """Unittest TestCase subclass"""
    def test_1_id_assign(self):
        """Method validates ID attribute assignment"""
        b = Base()
        self.assertEqual(b.id, 1)
        b1 = Base()
        self.assertEqual(b1.id, 2)
        b2 = Base(12)
        self.assertEqual(b2.id, 12)
        self.assertEqual(b.id, 1)
        b2.id = 999
        self.assertEqual(b2.id, 999)
