import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
    
    def test_add_negative(self):
        self.assertEqual(self.calc.add(-1, -2), -3)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(1,2),-1)

    def test_subtract_negative(self):
        self.assertEqual(self.calc.subtract(-1,-2),1)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2,0),0)

    def test_multiply_negative(self):
        self.assertEqual(self.calc.multiply(-1,-2),2)
    
    def test_divide_first_morethan_sec(self):
         self.assertEqual(self.calc.divide(6,3),2)

    def test_divide_first_morethan_sec_negative(self):
         self.assertEqual(self.calc.divide(6,-3),-2)

    def test_modulo_first_morethan_sec(self):
         self.assertEqual(self.calc.modulo(6,3),0)

    def test_modulo_first_morethan_sec_negative(self):
         self.assertEqual(self.calc.modulo(-6,-3),0)

    


    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()