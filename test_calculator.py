import unittest
from faker import Faker
import calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.fake = Faker()

    def test_add(self):
        for _ in range(5):
            num1 = self.fake.random_int(0, 100)
            num2 = self.fake.random_int(0, 100)
            self.assertEqual(calculator.add(num1, num2), num1 + num2)

    def test_subtract(self):
        for _ in range(5):
            num1 = self.fake.random_int(0, 100)
            num2 = self.fake.random_int(0, 100)
            self.assertEqual(calculator.subtract(num1, num2), num1 - num2)

    def test_multiply(self):
        for _ in range(5):
            num1 = self.fake.random_int(0, 100)
            num2 = self.fake.random_int(0, 100)
            self.assertEqual(calculator.multiply(num1, num2), num1 * num2)

    def test_divide(self):
        for _ in range(5):
            num1 = self.fake.random_int(0, 100)
            num2 = self.fake.random_int(1, 100)  # Ensure num2 is not zero
            self.assertEqual(calculator.divide(num1, num2), num1 / num2)

if __name__ == '__main__':
    unittest.main()
