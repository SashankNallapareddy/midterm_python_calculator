import calculator
import autotest
import conversions

def main():
    """Main function to run the program."""
    while True:
        print("Select operation:")
        print("1. Use Calculator")
        print("2. Autotest")
        print("3. Convert Metric")
        print("4. Exit")
        choice = input("Enter choice (1/2/3/4): ")

        if choice == '1':
            calculator.menu()
        elif choice == '2':
            autotest.autotest()
        elif choice == '3':
            try:
                
                result = conversions.convert_metric(value, from_unit, to_unit)
                print(f"Result: {value} {from_unit} = {result} {to_unit}")
            except ValueError as e:
                print(f"Error: {e}")
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
