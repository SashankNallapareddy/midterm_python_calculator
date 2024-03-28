import os
import logging
from commandManager import CommandManager
from history import History


# Retrieve the value of the LOG_LEVEL environment variable
# Configure logging to output only to file
log_level = os.getenv("LOG_LEVEL", "INFO")
logging.basicConfig(filename='calculator.log',
                    level=logging.getLevelName(log_level),
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Initialize History object
history = History()

def get_valid_float_input(prompt):
    """Prompt user for a valid float input."""
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")



def save_calculation(a, op, b, result , operator):
    if operator == 'null':
        history.save_to_csv(a, op, b, result , operator)
        print("Calculation saved successfully.")   
        """Save a calculation to history."""
    else:
        history.save_to_csv(a, op, b, result , operator)
        print("Calculation saved successfully.")

def view_history():
    """View the history of saved calculations."""
    history.show_history()




def process_command(command_str):
    """Process a user-defined command (hidden functionality)."""
    # Split the command string into parts
    parts = command_str.split()

    # Check if the first part is a valid command
    if parts[0] in ['add', 'subtract', 'multiply', 'divide' , 'custom']:
        try:
            # Extract operands
            num1 = get_valid_float_input("Enter first number: ")
            num2 = get_valid_float_input("Enter second number: ")
            if parts[0] == 'custom':
                operator= input("Enter operation you want to perform: ")

            # Call the corresponding function based on command
            if parts[0] == 'add':
                result = CommandManager.add(num1, num2)
                operator='null'
            elif parts[0] == 'subtract':
                result = CommandManager.subtract(num1, num2)
                operator='null'
            elif parts[0] == 'multiply':
                result = CommandManager.multiply(num1, num2)
                operator='null'
            elif parts[0] == 'divide':
                result = CommandManager.divide(num1, num2)
                operator='null'
            elif parts[0] == 'custom':
                result = CommandManager.custom_action(num1, num2 , operator)

            print("Result:", result)

            # Ask to save calculation
            save = input("Do you want to save this calculation? (yes/no): ")
            if save.lower() == 'yes' and parts[0] != 'custom':
                save_calculation(num1, parts[0], num2, result , operator)
            elif save.lower() == 'yes':
                save_calculation(num1, parts[0], num2, result , operator)
        except Exception as e:
            print(f"Error: {e}")
    else:
        print(f"Invalid command: {command_str}")  # Optional: Inform user about the hidden functionality


def menu():
    """Display calculator menu and handle user input."""
    while True:
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Custom Action")
        print("6. View History")
        print("7. Exit")  # Removed custom command option

        choice = input("Enter choice (1/2/3/4/5/6/7): ")

        if choice in ('1', '2', '3', '4' ,'5'):
            # Perform calculations based on menu choice
            operation = {
                '1': 'add',
                '2': 'subtract',
                '3': 'multiply',
                '4': 'divide',
                '5': 'custom'
            }[choice]
            process_command(operation)
        elif choice == '6':
            view_history()
        elif choice == '7':
            break  # Exit the calculator
        else:
            print("Invalid Input")


# If this script is executed directly, run the menu
if __name__ == "__main__":
    menu()
