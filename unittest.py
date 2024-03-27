import unittest
import calculator

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(1, 2), 3)
        self.assertEqual(calculator.add(5, -2), 3)
        self.assertEqual(calculator.add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(5, 2), 3)
        self.assertEqual(calculator.subtract(5, -2), 7)
        self.assertEqual(calculator.subtract(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(calculator.multiply(2, 3), 6)
        self.assertEqual(calculator.multiply(5, -2), -10)
        self.assertEqual(calculator.multiply(0, 10), 0)

    def test_divide(self):
        self.assertEqual(calculator.divide(6, 2), 3)
        self.assertEqual(calculator.divide(5, -2), -2.5)
        with self.assertRaises(ValueError):
            calculator.divide(6, 0)

if __name__ == '__main__':
    unittest.main()
