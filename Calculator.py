while True:
    print("\n1.Addition 2.Subtraction 3.Multiplication 4.Division 5.Exit")
    choice = input("Enter your choice (1-5): ")
    if choice == '5':
        print("Exiting...")
        break
    if choice not in ['1', '2', '3', '4']:
        print("Invalid choice! Please enter a number between 1-5.")
        continue
    n1 = float(input("Enter the first number: "))
    n2 = float(input("Enter the second number: "))
    if choice == '1':
        result = n1 + n2
        print(f"Addition of {n1} and {n2} is {result}")
    elif choice == '2':
        result = n1 - n2
        print(f"Subtraction of {n1} and {n2} is {result}")
    elif choice == '3':
        result = n1 * n2
        print(f"Multiplication of {n1} and {n2} is {result}")
    elif choice == '4':
        if n2 != 0:
            result = n1 / n2
            print(f"Division of {n1} by {n2} is {result}")
        else:
            print("Error: Division by zero is not allowed.")
