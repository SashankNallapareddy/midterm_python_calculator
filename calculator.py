import logging

# Configure logging
logging.basicConfig(filename='calculator.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def add(x, y):
    result = x + y
    logging.info(f"Add: {x} + {y} = {result}")
    return result

def subtract(x, y):
    result = x - y
    logging.info(f"Subtract: {x} - {y} = {result}")
    return result

def multiply(x, y):
    result = x * y
    logging.info(f"Multiply: {x} * {y} = {result}")
    return result

def divide(x, y):
    if y == 0:
        logging.error("Division by zero!")
        raise ValueError("Cannot divide by zero!")
    result = x / y
    logging.info(f"Divide: {x} / {y} = {result}")
    return result