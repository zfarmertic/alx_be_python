import unnittest
from simple_calculator import SimpleCalculator

class TestCalc(unnittest.TestCase):
    def calc(self):
        self.calc = SimpleCalculator()
    
    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
    