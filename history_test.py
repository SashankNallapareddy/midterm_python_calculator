import unittest
from faker import Faker
import calculator
import pytest
from commandManager import CommandManager


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
            self.assertEqual(CommandManager.add(num1, num2), num1 + num2)

    def test_subtract(self):
        """Test the subtract function."""
        for _ in range(5):
            num1 = self.fake.random_int(0, 100)
            num2 = self.fake.random_int(0, 100)
            self.assertEqual(CommandManager.subtract(num1, num2), num1 - num2)

    def test_multiply(self):
        """Test the multiply function."""
        for _ in range(5):
            num1 = self.fake.random_int(0, 100)
            num2 = self.fake.random_int(0, 100)
            self.assertEqual(CommandManager.multiply(num1, num2), num1 * num2)

    def test_divide(self):
        """Test the divide function."""
        for _ in range(5):
            num1 = self.fake.random_int(0, 100)
            num2 = self.fake.random_int(1, 100)  # Ensure num2 is not zero
            self.assertEqual(CommandManager.divide(num1, num2), num1 / num2)

@pytest.fixture
def history():
    from history import History
    return History()

def test_save_to_csv(history):
    a = 10
    op = '+'
    b = 5
    result = 15
    operator = 'null'
    history.save_to_csv(a, op, b, result, operator)
    # Assert that the CSV file is created and contains the saved calculation
    # You can use your own assertions here based on your specific requirements

def test_show_history(history, capsys):
    # Assuming the CSV file already exists with some saved calculations
    history.show_history()
    captured = capsys.readouterr()
    # Assert that the captured output matches the expected output
    # You can use your own assertions here based on your specific requirements

if __name__ == '__main__':
    unittest.main()