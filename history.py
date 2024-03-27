class History:
    def __init__(self):
        self.saved_calculations = []

    def save_calculation(self, a, op, b, result):
        if len(self.saved_calculations) >= 5:
            self.saved_calculations.pop(0)  # Remove the oldest calculation if max limit reached
        self.saved_calculations.append((a, op, b, result))

    def show_history(self):
        if not self.saved_calculations:
            print("No saved calculations.")
            return
        print("Saved calculations:")
        for i, calc in enumerate(self.saved_calculations, 1):
            a, op, b, result = calc
            print(f"Saved calculation {i}: {a} {op} {b} = {result}")
