class History:
    """Class to manage the history of saved calculations.

    This class provides functionality to save calculations and display the history
    of saved calculations.

    Attributes:
        saved_calculations (list): List to store saved calculations.
    """

    def __init__(self):
        """Initialize the History object."""
        self.saved_calculations = []

    def save_calculation(self, a, op, b, result):
        """Save a calculation to history.

        Args:
            a (float): The first number in the calculation.
            op (str): The operator used in the calculation.
            b (float): The second number in the calculation.
            result (float): The result of the calculation.
        """
        if len(self.saved_calculations) >= 5:
            self.saved_calculations.pop(0)  # Remove the oldest calculation if max limit reached
        self.saved_calculations.append((a, op, b, result))

    def show_history(self):
        """Display the history of saved calculations."""
        if not self.saved_calculations:
            print("No saved calculations.")
            return
        print("Saved calculations:")
        for i, calc in enumerate(self.saved_calculations, 1):
            a, op, b, result = calc
            print(f"Saved calculation {i}: {a} {op} {b} = {result}")
