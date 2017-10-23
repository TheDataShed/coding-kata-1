import unittest
from string_calculator import add

class test_string_calculator(unittest.TestCase):


    def test_empty_string(self):
        """
        Tests to see if an empty string returns 0.
        """
        self.assertEqual( add(""), 0)

    def test_1_number(self):
        """
        Tests that a single number returns it's value.
        """
        self.assertEqual(add("1"), 1)
        self.assertEqual(add("2"), 2)

    def test_2_numbers(self):
        """
        Tests that 2 numbers delimited by a comma returns the sum.
        """
        self.assertEqual(add("1,2"), 3)

    def test_multiple_numbers(self):
        """
        Tests that multiple(an unknown amount of?) numbers delimited by a comma returns the sum.
        """
        self.assertEqual(add("1,2,3,10"), 16)

    def test_newline_2_numbers(self):
        """
        Tests that sum is still returned when numbers are delimited by a newline instead of comma.
        """
        self.assertEqual(add("1\n2"), 3)

    def test_newline_multiple_numbers(self):
        """
        Tests that sum is still returned when numbers are delimited by a newline instead of comma for multiple numbers.
        """
        self.assertEqual(add("1\n2\n3"), 6)

    def test_different_delimiters(self):
        """
        Tests that sum is still returned when various delimiters are used.
        """
        self.assertEqual(add("//£\n1£2"), 3)

    def test_negative_numbers(self):
        """
        Tests that negatives are ignored
        """
        self.assertEqual(add("1, -2"), 1)

    def test_greater_than_1000_ignored(self):
        """
        Tests that numbers greater than 1000 are ignored
        """
        self.assertEqual(add("1,1001"), 1)

    def test_delimiters_any_length(self):
        """
        Tests that delimiters can be any length.
        """
        self.assertEqual(add("//---\n1---3---5"), 9)

    def test_multi_delims_any_length(self):
        """
        Tests that multiple delimiters of any length can be used as input
        """
        self.assertEqual(add("//£$%\n1£$%3£$%5"), 9)





if __name__ == '__main__':
    unittest.main()
