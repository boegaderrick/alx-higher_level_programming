#!/usr/bin/python3
"""Unittest for Rectangle class"""
import unittest
import io
import os
from unittest.mock import patch
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Derived class of the TestCase class"""

    def test_1_values(self):
        """Method checks if values reflect as assigned"""
        n = Rectangle(3, 5, 2, 8)

        self.assertEqual(n.id, 1)
        self.assertEqual(n.x, 2)
        self.assertEqual(n.width, 3)
        self.assertEqual(n.height, 5)
        self.assertEqual(n.y, 8)

    def test_2_gets_sets(self):
        """Method checks setters and getters"""
        r = Rectangle(7, 4, 9, 1)

        self.assertEqual(r.id, 2)
        r.id = 100
        self.assertEqual(r.id, 100)
        r.width = 39
        self.assertEqual(r.width, 39)
        r.height = 97
        self.assertEqual(r.height, 97)
        r.x = 67
        self.assertEqual(r.x, 67)
        r.y = 23
        self.assertEqual(r.y, 23)

    def test_3_raises(self):
        """Method checks if exceptions are raised as necessary"""
        i = Rectangle(5, 34, 93, 9, 999)

        with self.assertRaises(ValueError):
            i.height = -9
        with self.assertRaises(ValueError):
            i.width = -1
        with self.assertRaises(TypeError):
            i.height = None
        with self.assertRaises(TypeError):
            i.width = 'hello'
        with self.assertRaises(ValueError):
            i.x = -1
        with self.assertRaises(TypeError):
            i.y = 5.4

    def test_4_area(self):
        """Method checks the return of the class area() method"""
        r = Rectangle(7, 3, 5, 9, 10)
        self.assertEqual(r.area(), 21)
        r.width = 3
        r.height = 2
        self.assertEqual(r.area(), 6)
        r.width = 2
        r. height = 10
        self.assertEqual(r.area(), 20)
        r.width = 1985
        r.height = 7564
        self.assertEqual(r.area(), 15014540)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_5_display(self, mock_stdout):
        """Method checks the output of the display method"""
        r = Rectangle(4, 5)
        r.display()
        output = mock_stdout.getvalue()
        self.assertEqual(output, '####\n####\n####\n####\n####\n')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_6_display(self, mock_stdout):
        """Display method output unittest"""
        r = Rectangle(6, 3, 5, 2, 198)
        r.display()
        output = mock_stdout.getvalue()
        self.assertEqual(output, '\n\n     ######\n     ######\n     ######\n')

    def test_6__str__(self):
        """Method checks the return of __str__"""
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(r.__str__(), '[Rectangle] (12) 2/1 - 4/6')
        r = Rectangle(5, 5, 1)
        self.assertEqual(r.__str__(), '[Rectangle] (4) 1/0 - 5/5')
        r = Rectangle(99, 88, id=101)
        self.assertEqual(r.__str__(), '[Rectangle] (101) 0/0 - 99/88')

    def test_7_update(self):
        """Checks class update method"""
        r = Rectangle(9, 23, 5, 7, 88)
        r.update(987)
        self.assertEqual(r.id, 987)
        r.update(8, 2, 3, 4, 5)
        self.assertEqual(r.id, 8)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)
        r.update(y=565, id = 287)
        self.assertEqual(r.id, 287)
        self.assertEqual(r.y, 565)

    def test_8__dict__(self):
        """Unittest for class to_dictionary method"""
        r = Rectangle(32, 45, 23, 88, 901)
        self.assertEqual(r.to_dictionary(), {'x': 23, 'y': 88, 'id': 901, 
                                            'height': 45, 'width': 32})

    def test_9_serialization(self):
        """Unit test for object json representation"""
        r = Rectangle(8, 3, 5, 2, 101)
        d = r.to_dictionary()
        jsn = Rectangle.to_json_string([d])
        self.assertTrue(type(jsn) is str)
        self.assertEqual(jsn, '[{"x": 5, "y": 2, "id": 101, "height": 3, "width": 8}]')
        jsn = Rectangle.to_json_string(None)
        self.assertEqual(jsn, '[]')
        jsn = Rectangle.to_json_string([])
        self.assertEqual(jsn, '[]')

    def test_10_json_file(self):
        """Test for json file creation"""
        r = Rectangle(8, 3, 5, 2, 101)
        Rectangle.save_to_file([r])
        with open('Rectangle.json', mode='r', encoding='utf=8') as file:
            content = file.read()
        self.assertEqual(content, '[{"x": 5, "y": 2, "id": 101, "height": 3, "width": 8}]')
        os.remove('Rectangle.json')

        Rectangle.save_to_file([])
        with open('Rectangle.json', mode='r', encoding='utf=8') as file:
            content = file.read()
        self.assertEqual(content, '[]')
        os.remove('Rectangle.json')

        Rectangle.save_to_file(None)
        with open('Rectangle.json', mode='r', encoding='utf=8') as file:
            content = file.read()
        self.assertEqual(content, '[]')
        os.remove('Rectangle.json')

    def test_11_json_to_dict(self):
        """Tests json deserialization"""
        r = Rectangle(8, 3, 5, 2, 101)
        json_str = Rectangle.to_json_string([r.to_dictionary()])
        lst = Rectangle.from_json_string(json_str)
        self.assertEqual(lst, [{"x": 5, "y": 2, "id": 101, "height": 3, "width": 8}])
        lst = Rectangle.from_json_string('[]')
        self.assertEqual(lst, [])
        lst = Rectangle.from_json_string(None)
        self.assertEqual(lst, [])







if __name__ == '__main__':
    unittest.main()
