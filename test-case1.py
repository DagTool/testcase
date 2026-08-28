import unittest
from loop import process_even_numbers

class TestFunction(unittest.TestCase):

    def test_numbers_are_processed_correctly(self):
        """
        Input: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        Expected Output: [2, 4, 6, 8, 10]
        """
        input_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected_output = [2, 4, 6, 8, 10]
        actual_output = process_even_numbers(input_data)
        self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main()
