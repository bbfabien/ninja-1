#!/usr/bin/python3.5

import unittest
import sources.addition as code

class Test(unittest.TestCase):

    def setUp(self):
    	pass

    def test_a_isNaN(self):
        a = 'p'
        b = 32
        result = code.addition(a, b)
        self.assertEqual(result, 'NaN')

    def test_b_number(self):
        a = 2
        b = 5
        result = code.addition(a, b)
        self.assertTrue(isinstance(result, int))

    def test_c_correctResult(self):
        a = 23
        b = 54
        result = code.addition(a, b)
        self.assertEqual(result, 77)

if __name__ == '__main__':
	unittest.main()
