import calculator

def main():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        if choice == '1':
            result = calculator.add(num1, num2)
        elif choice == '2':
            result = calculator.subtract(num1, num2)
        elif choice == '3':
            result = calculator.multiply(num1, num2)
        elif choice == '4':
            try:
                result = calculator.divide(num1, num2)
            except ValueError as e:
                print(e)
                return
        print("Result:", result)
    else:
        print("Invalid Input")

if __name__ == "__main__":
    main()
