print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

# Take user input for operation choice
choice = input("Enter choice (1/2/3/4): ")

# Check if the choice is valid
if choice not in ["1", "2", "3", "4"]:
    print("Invalid input")
else:
    # Take user input for two numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Perform the selected operation and display the result
    if choice == "1":
        print("Result:", num1 + num2)
    elif choice == "2":
        print("Result:", num1 - num2)
    elif choice == "3":
        print("Result:", num1 * num2)
    elif choice == "4":
        if num2 == 0:
            print("Cannot divide by zero")
        else:
            print("Result:", num1 / num2)
