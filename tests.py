import unittest
from task1 import y
from task2 import res,y1
from task3 import match
from task4 import task4
from task5 import y2


class Testing(unittest.TestCase):
    def test_string1(self):
        b = ['adana@gmail', 'roewq@icloud', 'qqq@mail']
        self.assertEqual(y, b)
        self.assertIn('adana@gmail',y)
        self.assertEqual(list, type(y))

    def test_string2(self):
        self.assertEqual('12/12/2022', res)
        self.assertNotEquals(y1, res)

    def test_string3(self):
        self.assertEqual(type(match),list)
        self.assertEqual(match[0], "london")
        self.assertEqual(match[1], "gmail.org")

    def test_string4(self):
        number = '380964329919'
        self.assertEqual(task4(number), number)
        with self.assertRaises(AttributeError):
            task4('210985683498')

    def test_string5(self):
        self.assertEqual(type(y2), list)
        self.assertEqual(len(y2), 11)