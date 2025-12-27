import unittest
from simple_calculator import SimpleCalculator

class TestCalc(unnittest.TestCase):
    def calc(self):
        self.calc = SimpleCalculator()
    
    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(4, 2), 6)
        self.assertEqual(self.calc.subtract(2, 2), 0)
    def test_division(self):
        self.assertEqual(self.calc.divide(2, 2), 1)
        self.assertEqual(self.calc.divide(4, 2), 2)
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(2, 2), 4)
        self.assertEqual(self.calc.multiply(4, 2), 8)