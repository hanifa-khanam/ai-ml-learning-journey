from expense_tracker import ExpenseTracker
from transactions import Transaction

tracker = ExpenseTracker()
tracker.load_from_file()



while True:
    print("\n--- Personal Expense Tracker ---")
    print("1. Add Transaction")
    print("2. Delete Transaction")
    print("3. Update Transaction")
    print("4. View All Transactions")
    print("5. View Summary")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        try:
            id = int(input("Enter transaction ID: "))
            amount = float(input("Enter amount: "))
            transaction_type = input("Enter type (income/expense): ").lower()
            if transaction_type not in ["income", "expense"]:
                print("Invalid type! Must be 'income' or 'expense'.")
                continue
            category = input("Enter category: ")
            date = input("Enter date (e.g., December 2, 2025): ")
            description = input("Enter description: ")

            t = Transaction(id, amount, transaction_type, category, date, description)
            tracker.add_transaction(t)
        except ValueError:
            print("Invalid input! ID must be integer and amount must be numeric.")

    elif choice == "2":
        try:
            transaction_id = int(input("Enter transaction ID to delete: "))
            tracker.delete_transaction(transaction_id)
        except ValueError:
            print("Invalid input! ID must be integer.")

    elif choice == "3":
        try:
            transaction_id = int(input("Enter transaction ID to update: "))
            tracker.update_transaction(transaction_id)
        except ValueError:
            print("Invalid input! ID must be integer.")

    elif choice == "4":
        tracker.view_transactions()

    elif choice == "5":
        tracker.view_summary()

    elif choice == "6":
        tracker.save_to_file()
        print("Goodbye! Data saved successfully.")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 6.")

