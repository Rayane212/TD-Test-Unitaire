import unittest
from calculatrice import Calculatrice

class TestCalculatrice(unittest.TestCase):
    
    def setUp(self):
        self.calc = Calculatrice()
    
    def test_addition(self):
        self.assertEqual(self.calc.addition(5, 3), 8)
        self.assertEqual(self.calc.addition(-1, 1), 0)
        self.assertEqual(self.calc.addition(0, 0), 0)
        self.assertEqual(self.calc.addition(-5, -3), -8)
    
    def test_soustraction(self):
        self.assertEqual(self.calc.soustraction(10, 4), 6)
        self.assertEqual(self.calc.soustraction(5, 10), -5)
        self.assertEqual(self.calc.soustraction(0, 0), 0)
        self.assertEqual(self.calc.soustraction(-5, -5), 0)
    
    def test_multiplication(self):
        self.assertEqual(self.calc.multiplication(6, 7), 42)
        self.assertEqual(self.calc.multiplication(0, 5), 0)
        self.assertEqual(self.calc.multiplication(-3, 4), -12)
        self.assertEqual(self.calc.multiplication(-3, -4), 12)
    
    def test_division(self):
        self.assertEqual(self.calc.division(15, 3), 5)
        self.assertEqual(self.calc.division(10, 2), 5)
        self.assertEqual(self.calc.division(-10, 2), -5)
        self.assertEqual(self.calc.division(-10, -2), 5)
        self.assertEqual(self.calc.division(0, 5), 0)
        self.assertAlmostEqual(self.calc.division(1, 3), 0.3333333333333333)
    
    def test_division_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc.division(10, 0)

    def test_exponentiation(self):
        self.assertEqual(self.calc.exponentiation(2, 3), 8)
        self.assertEqual(self.calc.exponentiation(5, 0), 1)
        self.assertEqual(self.calc.exponentiation(0, 5), 0)
        self.assertEqual(self.calc.exponentiation(-2, 3), -8)
        self.assertEqual(self.calc.exponentiation(-2, 2), 4)

if __name__ == "__main__":
    unittest.main()