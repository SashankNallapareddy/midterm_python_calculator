import os
import pandas as pd

class History:
    @staticmethod
    def save_to_csv(a, op, b, result, operator):
        """Static method to save a calculation to a CSV file."""
        file_name = os.getenv("HISTORY_CSV_FILE", "history.csv")
        if operator == 'null':
            data = {'Operand1': [a], 'Operator': [op], 'Operand2': [b], 'Result': [result]}
        else:
            data = {'Operand1': [a], 'Operator': [operator], 'Operand2': [b], 'Result': [result]}
        df = pd.DataFrame(data)
        if os.path.exists(file_name):
            # Read existing history
            history_df = pd.read_csv(file_name)
            # Concatenate existing history with new calculation
            history_df = pd.concat([history_df, df], ignore_index=True)
            # Keep only the most recent 5 calculations
            history_df = history_df.tail(5)
            # Save to CSV
            history_df.to_csv(file_name, index=False)
        else:
            df.to_csv(file_name, index=False)


    @staticmethod
    def show_history():
        """Static method to display the history of saved calculations."""
        file_name = os.getenv("HISTORY_CSV_FILE", "history.csv")
        if not os.path.exists(file_name):
            print("No saved calculations.")
            return
        try:
            df = pd.read_csv(file_name)
            if df.empty:
                print("No saved calculations.")
                return
            print("Saved calculations:")
            for i, row in df.iterrows():
                print(f"Saved calculation {i+1}: {row['Operand1']} {row['Operator']} {row['Operand2']} = {row['Result']}")
        except pd.errors.EmptyDataError:
            print("No saved calculations.")
