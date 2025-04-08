import unittest
from fizzbuzz import FizzBuzz

class TestFizzBuzz(unittest.TestCase):
    def setUp(self):
        self.fizzbuzz = FizzBuzz()

    def test_fizzbuzz(self):
        expected_output = [
            1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz",
            11, "Fizz", 13, 14, "FizzBuzz"
        ]
        result = list(self.fizzbuzz.fizzbuzz(15))
        self.assertEqual(result, expected_output)
   
    if __name__ == "__main__":
        unittest.main()