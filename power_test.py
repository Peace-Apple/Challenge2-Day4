import unittest
from power import power

class Test_power(unittest.TestCase):

    def test_power(self):
        self.assertEqual(power(3, 2), pow(3, 2))
    
    def test_negative_power(self):
        self.assertEqual(power(2, -3), pow(2, -3))

    def test_both_negative(self):
        self.assertEqual(power(-1, -1), pow(-1, -1))

    def test_float_power(self):
        self.assertEqual(power(-2.0, 0.5), 'invalid input')

    def test_input_integer_or_float(self):
        self.assertEqual(power('x', 2), 'invalid input')


if __name__ == '__main__':
    unittest.main()