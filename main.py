import calculator
import autotest

def main():
    """Main function to run the program."""
    while True:
        print("Select operation:")
        print("1. Use Calculator")
        print("2. Autotest")
        print("3. Exit")
        choice = input("Enter choice (1/2/3): ")

        if choice == '1':
            calculator.menu()
        elif choice == '2':
            autotest.autotest()
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
