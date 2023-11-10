# test_functions.py
import unittest
from functions import add_numbers, multiply_numbers, divide_numbers

class TestMathFunctions(unittest.TestCase):

    def test_add_numbers(self):
        self.assertEqual(add_numbers(3, 5), 8)
        self.assertEqual(add_numbers(-2, 7), 5)
        self.assertEqual(add_numbers(0, 0), 0)

    def test_multiply_numbers(self):
        self.assertEqual(multiply_numbers(3, 5), 15)
        self.assertEqual(multiply_numbers(-2, 7), -14)
        self.assertEqual(multiply_numbers(0, 5), 0)

    def test_divide_numbers(self):
        self.assertEqual(divide_numbers(10, 1), 5)
        self.assertEqual(divide_numbers(-6, 3), -2)
        
        with self.assertRaises(ValueError):
            divide_numbers(8, 0)

if __name__ == '__main__':
    unittest.main()
