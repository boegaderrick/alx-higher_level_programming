#!/usr/bin/python3
"""Square class unittest module"""
import unittest
import os
from models.square import Square
from models.rectangle import Rectangle


class TestSquare(unittest.TestCase):
    """Test case subclass"""
    def test_1__str__(self):
        """Checks string representaion of object"""
        s = Square(50, 6, 3, 989)
        self.assertEqual(s.__str__(), '[Square] (989) 6/3 - 50')
        s = Square(1, 1, 1)
        self.assertEqual(s.__str__(), '[Square] (1) 1/1 - 1')

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
        with self.assertRaises(TypeError):
            s.size = 'k'
        with self.assertRaises(ValueError):
            s.size = 0

    def test_3_types(self):
        """Checks inheritance"""
        s = Square(3)
        self.assertTrue(isinstance(s, Rectangle))

    def test_4_sets_gets(self):
        """Checks setters and getters of square class"""
        s = Square(3, 3, 3, 333)
        s.size = 27
        self.assertEqual(s.size, 27)
        self.assertEqual(s.width, 27)
        self.assertEqual(s.height, 27)

    def test_5_square_update(self):
        s = Square(6, 3, 4, 343)
        self.assertEqual(s.__str__(), '[Square] (343) 3/4 - 6')
        s.update(88)
        self.assertEqual(s.id, 88)
        s.update(size=102)
        self.assertEqual(s.height, 102)
        s.update(y=98, x=89)
        self.assertEqual(s.__str__(), '[Square] (88) 89/98 - 102')

    def test_6__dict__(self):
        """Unittest for class to_dictionary method"""
        s = Square(32, 23, 88, 901)
        self.assertEqual(s.to_dictionary(), {'id': 901, 'x': 23, 'size': 32, 'y': 88})

    def test_7_serialization(self):
        """Test conversion to json"""
        s = Square(8, 5, 2, 101)
        d = s.to_dictionary()
        jsn = Square.to_json_string([d])
        self.assertTrue(type(jsn) is str)
        self.assertEqual(jsn, '[{"id": 101, "x": 5, "size": 8, "y": 2}]')
        jsn = Square.to_json_string(None)
        self.assertEqual(jsn, '[]')
        jsn = Square.to_json_string([])
        self.assertEqual(jsn, '[]')

    def test_10_json_file(self):
        """Unit test for saving json string to file"""
        s = Square(8, 5, 2, 101)
        Square.save_to_file([s])
        with open('Square.json', mode='r', encoding='utf=8') as file:
            content = file.read()
        self.assertEqual(content, '[{"id": 101, "x": 5, "size": 8, "y": 2}]')
        os.remove('Square.json')

        Square.save_to_file([])
        with open('Square.json', mode='r', encoding='utf=8') as file:
            content = file.read()
        self.assertEqual(content, '[]')
        os.remove('Square.json')

        Square.save_to_file(None)
        with open('Square.json', mode='r', encoding='utf=8') as file:
            content = file.read()
        self.assertEqual(content, '[]')
        os.remove('Square.json')

    def test_11_json_to_dict(self):
        """Tests json deserialization"""
        s = Square(8, 5, 2, 101)
        json_str = Square.to_json_string([s.to_dictionary()])
        lst = Square.from_json_string(json_str)
        self.assertEqual(lst, [{"id": 101, "x": 5, "size": 8, "y": 2}])
        lst = Square.from_json_string('[]')
        self.assertEqual(lst, [])
        lst = Square.from_json_string(None)
        self.assertEqual(lst, [])




if __name__ == '__main__':
    unittest.main()
