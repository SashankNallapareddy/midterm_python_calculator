"""Autotest Module

This module provides functionality for generating fake data and performing automated tests
on the calculator module.

Functions:
    autotest: Generate fake data and perform automated tests.
"""

import coverage
from faker import Faker
import calculator
from commandManager import CommandManager


command = CommandManager()
# Start coverage
cov = coverage.Coverage()
cov.start()

def autotest():
    """Generate fake data and perform automated tests."""
    fake = Faker()

    for _ in range(20):
        num1 = fake.random_int(0, 100)
        num2 = fake.random_int(1, 100)

        print(f"Testing with numbers: {num1}, {num2}")

        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")

        choice = fake.random_element(elements=('1', '2', '3', '4'))

        if choice == '1':
            result = command.add(num1, num2)
        elif choice == '2':
            result = command.subtract(num1, num2)
        elif choice == '3':
            result = command.multiply(num1, num2)
        elif choice == '4':
            try:
                result = command.divide(num1, num2)
            except ValueError as e:
                print(e)
                continue
        print("Result:", result)
    # Stop coverage
    cov.stop()

    # Save coverage report
    cov.save()

    # Generate coverage report
    cov.report()

if __name__ == "__main__":
    # Perform autotest if executed as a script
    autotest()
