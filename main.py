import calculator
import autotest

def main():
    print("Select operation:")
    print("1. Use Calculator")
    print("2. Autotest")
    choice = input("Enter choice (1/2): ")

    if choice == '1':
        calculator.menu()
    elif choice == '2':
        autotest.autotest()
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
