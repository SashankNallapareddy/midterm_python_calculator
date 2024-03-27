import logging
from history import History  # Import History class from history.py

# Configure logging to output only to file
logging.basicConfig(filename='calculator.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize History object
history = History()

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

def save_calculation(a, op, b, result):
    """Save a calculation to history."""
    history.save_calculation(a, op, b, result)
    print("Calculation saved successfully.")

def view_history():
    """View the history of saved calculations."""
    history.show_history()

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
    while True:
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. View History")
        print("6. Exit")

        choice = input("Enter choice (1/2/3/4/5/6): ")

        if choice in ('1', '2', '3', '4'):
            try:
                num1 = get_valid_float_input("Enter first number: ")
                num2 = get_valid_float_input("Enter second number: ")
                operation = {
                    '1': '+',
                    '2': '-',
                    '3': '*',
                    '4': '/'
                }[choice]
                if choice == '4' and num2 == 0:
                    raise ValueError("Cannot divide by zero!")
                result = eval(f"{num1} {operation} {num2}")
                print("Result:", result)
                save = input("Do you want to save this calculation? (yes/no): ")
                if save.lower() == 'yes':
                    save_calculation(num1, operation, num2, result)
            except Exception as e:
                print(f"Error: {e}")
        elif choice == '5':
            view_history()
        elif choice == '6':
            break  # Exit the calculator
        else:
            print("Invalid Input")

# If this script is executed directly, run the menu
if __name__ == "__main__":
    menu()
