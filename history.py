import os
import pandas as pd

class History:
    @staticmethod
    def save_to_csv(a, op, b, result):
        """Static method to save a calculation to a CSV file."""
        file_name = os.getenv("HISTORY_CSV_FILE", "history.csv")
        data = {'Operand1': [a], 'Operator': [op], 'Operand2': [b], 'Result': [result]}
        df = pd.DataFrame(data)
        if os.path.exists(file_name):
            df.to_csv(file_name, mode='a', header=False, index=False)
        else:
            df.to_csv(file_name, index=False)

    @staticmethod
    def show_history():
        """Static method to display the history of saved calculations."""
        file_name = os.getenv("HISTORY_CSV_FILE", "history.csv")
        if not os.path.exists(file_name):
            print("No saved calculations.")
            return
        df = pd.read_csv(file_name)
        if df.empty:
            print("No saved calculations.")
            return
        print("Saved calculations:")
        for i, row in df.iterrows():
            print(f"Saved calculation {i+1}: {row['Operand1']} {row['Operator']} {row['Operand2']} = {row['Result']}")
