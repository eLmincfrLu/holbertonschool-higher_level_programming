#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Class to test max_integer function"""

    def test_ordered_list(self):
        """Test with an ordered list of integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test with an unordered list of integers"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Test with max value at the beginning"""
        self.assertEqual(max_integer([5, 4, 3, 2, 1]), 5)

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertEqual(max_integer([]), None)

    def test_one_element_list(self):
        """Test with a single element list"""
        self.assertEqual(max_integer([7]), 7)

    def test_floats(self):
        """Test with a list of floats"""
        self.assertEqual(max_integer([1.53, 6.33, -9.1, 4.8]), 6.33)

    def test_ints_and_floats(self):
        """Test with a mix of ints and floats"""
        self.assertEqual(max_integer([1.5, 3, 4.5, 2]), 4.5)

    def test_string(self):
        """Test with a string"""
        self.assertEqual(max_integer("Holberton"), 't')

    def test_list_of_strings(self):
        """Test with a list of strings"""
        self.assertEqual(max_integer(["apple", "pear", "banana"]), "pear")

    def test_negative_numbers(self):
        """Test with a list of negative numbers"""
        self.assertEqual(max_integer([-1, -5, -10, -2]), -1)

    if __name__ == "__main__":
        unittest.main()