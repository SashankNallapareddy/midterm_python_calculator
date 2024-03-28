import logging

class CommandManager:
    @staticmethod
    def add(x, y):
        """Add two numbers."""
        result = x + y
        logging.info(f"Add: {x} + {y} = {result}")
        return result

    @staticmethod
    def subtract(x, y):
        """Subtract two numbers."""
        result = x - y
        logging.info(f"Subtract: {x} - {y} = {result}")
        return result

    @staticmethod
    def multiply(x, y):
        """Multiply two numbers."""
        result = x * y
        logging.info(f"Multiply: {x} * {y} = {result}")
        return result

    @staticmethod
    def divide(x, y):
        """Divide two numbers."""
        if y == 0:
            logging.error("Division by zero!")
            raise ValueError("Cannot divide by zero!")
        result = x / y
        logging.info(f"Divide: {x} / {y} = {result}")
        return result

    @staticmethod
    def custom_action(x, y, operand):
        """Perform a custom action."""
        if operand == '^':
            result = x ** y
            logging.info(f"Custom action: {x} ^ {y} = {result}")
            return result
        else:
            raise ValueError("Invalid operand for custom action!")

    @staticmethod
    def perform_operation(operation, x, y, operand=None):
        """Perform the specified operation."""
        if operation == 'add':
            return CommandManager.add(x, y)
        elif operation == 'subtract':
            return CommandManager.subtract(x, y)
        elif operation == 'multiply':
            return CommandManager.multiply(x, y)
        elif operation == 'divide':
            return CommandManager.divide(x, y)
        elif operation == 'custom':
            return CommandManager.custom_action(x, y, operand)
        else:
            raise ValueError("Invalid operation!")
