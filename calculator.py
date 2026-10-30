
while True:
    print("\n===== PYTHON CALCULATOR =====")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

    choice = input("Choose an operation: ")

    if choice == "5":
        print("Calculator closed. Goodbye!")
        break

    if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice!")
        continue

   
