import logging

# Configure logging to output to both console and file
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.FileHandler('calculator.log'),
                        logging.StreamHandler()
                    ])

def add(x, y):
    """Add two numbers."""
    result = x + y
    logging.info(f"Add: {x} + {y} = {result}")
    return result

def subtract(x, y):
    """Subtract two numbers."""
    result = x - y
    logging.info(f"Subtract: {x} - {y} = {result}")
    return result

def multiply(x, y):
    """Multiply two numbers."""
    result = x * y
    logging.info(f"Multiply: {x} * {y} = {result}")
    return result

def divide(x, y):
    """Divide two numbers."""
    if y == 0:
        logging.error("Division by zero!")
        raise ValueError("Cannot divide by zero!")
    result = x / y
    logging.info(f"Divide: {x} / {y} = {result}")
    return result

def get_valid_float_input(prompt):
    """Prompt user for a valid float input."""
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def menu():
    """Display calculator menu and perform selected operation."""
    num1 = get_valid_float_input("Enter first number: ")
    num2 = get_valid_float_input("Enter second number: ")

    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        if choice == '1':
            result = add(num1, num2)
        elif choice == '2':
            result = subtract(num1, num2)
        elif choice == '3':
            result = multiply(num1, num2)
        elif choice == '4':
            try:
                result = divide(num1, num2)
            except ValueError as e:
                logging.error(str(e))
                print(e)
                return
        print("Result:", result)
    else:
        print("Invalid Input")
