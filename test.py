import unittest
from example2 import is_even


class TestExample2(unittest.TestCase):
    def test_is_even(self):
        self.assertTrue(is_even(100))
        self.assertTrue(is_even(2))
        self.assertTrue(is_even(0))
        self.assertTrue(is_even(-10))
        self.assertFalse(is_even(1))
        self.assertFalse(is_even(5))
        self.assertFalse(is_even(-51))

    def test_types(self):
        self.assertRaises(TypeError, is_even, 5+2j)
        self.assertRaises(TypeError, is_even, [1, 12, 3])
        self.assertRaises(TypeError, is_even, 'five')
        self.assertRaises(TypeError, is_even, '12')




if __name__ == "__main__":
    unittest.main()