import unittest
from unittest.mock import patch



from calculator import add, subtract, multiply, divide, get_valid_float_input, process_command, menu
import coverage

# Configure coverage
cov = coverage.Coverage()
cov.start()

class TestCalculator(unittest.TestCase):

    @patch('calculator.get_valid_float_input')
    def test_add(self, mock_get_input):
        # Use Faker to generate random numbers
        fake = faker.Faker()
        num1 = float(fake.pydecimal.Decimal(10, 2))
        num2 = float(fake.pydecimal.Decimal(10, 2))

        # Mock get_valid_float_input to return generated values
        mock_get_input.side_effect = [num1, num2]

        result = add(num1, num2)
        expected_result = num1 + num2

        self.assertEqual(result, expected_result)

    # ... other test cases as before ...

    @patch('sys.stdout')
    def test_menu(self, mock_stdout):
        # Test menu interactions (limited due to external input)
        # Simulate user choices (1 for add)
        user_choices = ['1']

        def mock_input(*args):
            return user_choices.pop(0)

        with patch('builtins.input', mock_input):
            menu()


if __name__ == '__main__':
    # Run tests and generate coverage report
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(TestCalculator))
    #cov.run(suite.run)
    cov.stop()
    cov.report()
