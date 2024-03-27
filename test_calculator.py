import unittest
from faker import Faker
import calculator

class TestCalculator(unittest.TestCase):
    """Test suite for the Calculator functions.

    This test suite contains unit tests for the add, subtract, multiply, and divide
    functions in the calculator module.

    Attributes:
        fake (Faker): A Faker instance for generating random test data.
    """

    def setUp(self):
        """Set up the test fixture."""
        self.fake = Faker()

    def test_add(self):
        """Test the add function."""
        for _ in range(5):
            num1 = self.fake.random_int(0, 100)
            num2 = self.fake.random_int(0, 100)
            self.assertEqual(calculator.add(num1, num2), num1 + num2)

    def test_subtract(self):
        """Test the subtract function."""
        for _ in range(5):
            num1 = self.fake.random_int(0, 100)
            num2 = self.fake.random_int(0, 100)
            self.assertEqual(calculator.subtract(num1, num2), num1 - num2)

    def test_multiply(self):
        """Test the multiply function."""
        for _ in range(5):
            num1 = self.fake.random_int(0, 100)
            num2 = self.fake.random_int(0, 100)
            self.assertEqual(calculator.multiply(num1, num2), num1 * num2)

    def test_divide(self):
        """Test the divide function."""
        for _ in range(5):
            num1 = self.fake.random_int(0, 100)
            num2 = self.fake.random_int(1, 100)  # Ensure num2 is not zero
            self.assertEqual(calculator.divide(num1, num2), num1 / num2)

if __name__ == '__main__':
    unittest.main()
