import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()
    #add cases
    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
    def test_add2(self):
        self.assertEqual(self.calc.add(-1, 2), 1)

    # Add the following test methods to the TestCalculator class:
    #subtract cases
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 4), 1)
    def test_subtract2(self):
        self.assertEqual(self.calc.subtract(0,  0), 0)

    #multiply cases
    def test_multiply_posive(self):
        self.assertEqual(self.calc.multiply(3,4), 12)
        self.assertEqual(self.calc.multiply(1,1), 1)
    def test_multiply_negative(self):
        self.assertEqual(self.calc.multiply(3,-4), -12)
        self.assertEqual(self.calc.multiply(-3,4), -12)
        self.assertEqual(self.calc.multiply(-3,-4), 12)
    def test_multiply_zero(self):
        self.assertEqual(self.calc.multiply(1,0),0)
        self.assertEqual(self.calc.multiply(0,1),0)
        self.assertEqual(self.calc.multiply(0,0),0)

    #divide cases
    # I assume that we
    def test_divide_positive(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(8, 2), 4)
    def test_divide_negative(self):
        self.assertEqual(self.calc.divide(-10, 2), -5)
        self.assertEqual(self.calc.divide(10, -2), -5)
        self.assertEqual(self.calc.divide(-10, -2), 5)
    def test_divide_zero_dividend(self):
        self.assertEqual(self.calc.divide(0, 5), 0)  
    def test_divide_by_zero(self):
        self.assertEqual(self.calc.divide(5, 0), "undefined")
        
    
    #modulo cases
    def test_modulo_positive(self):
        self.assertEqual(self.calc.modulo(7, 3), 1)
        self.assertEqual(self.calc.modulo(11, 3), 2)
    def test_modulo_negative_dividend(self):
        self.assertEqual(self.calc.modulo(-7, 3), -1) 
    def test_modulo_negative_divisor(self):
        self.assertEqual(self.calc.modulo(7, -3), 1)
    def test_modulo_zero_dividend(self):
        self.assertEqual(self.calc.modulo(0, 5), 0)
    def test_modulo_by_zero(self):
        self.assertEqual(self.calc.modulo(1,0),"undefined")
if __name__ == '__main__':
    unittest.main()