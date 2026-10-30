import csv
from datetime import datetime

FILENAME = "expenses.csv"

# Create file if it doesn't exist
try:
    open(FILENAME, "x").close()
except FileExistsError:
    pass


def add_expense():
    category = input("Enter category (Food, Transport, etc.): ")
    amount = float(input("Enter amount: "))
    date = datetime.now().strftime("%Y-%m-%d")

    with open(FILENAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount])

    print("✅ Expense added successfully!")


def view_expenses():
    print("\n--- Expense List ---")

    try:
        with open(FILENAME, "r") as file:
            reader = csv.reader(file)

            total = 0
            for row in reader:
                if row:
                    date, category, amount = row
                    print(f"Date: {date} | Category: {category} | Amount: ${amount}")
                    total += float(amount)

            print(f"\n💰 Total Expenses: ${total:.2f}")

    except FileNotFoundError:
        print("No expenses recorded yet.")


def main():
    while True:
        print("\n===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("❌ Invalid option. Try again.")


if __name__ == "__main__":
    main()
