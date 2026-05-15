from expense_tracker import ExpenseTracker
from transactions import Transaction
from visualization import (
    show_pie_chart,
    show_bar_chart,
    show_monthly_trend
)
tracker = ExpenseTracker()
tracker.load_from_file()
tracker.save_to_csv()



while True:
    print("\n--- Personal Expense Tracker ---")
    print("1. Add Transaction")
    print("2. Delete Transaction")
    print("3. Update Transaction")
    print("4. View All Transactions")
    print("5. View Summary")
    print("6. Show Bar Chart")
    print("7. Show Monthly trend")
    print("8. Exit")
    
    choice = input("Enter your choice (1-8): ")

    if choice == "1":
        try:
            transaction_id = int(input("Enter transaction ID: "))
            amount = float(input("Enter amount: "))
            transaction_type = input("Enter type (income/expense): ").lower()
            if transaction_type not in ["income", "expense"]:
                print("Invalid type! Must be 'income' or 'expense'.")
                continue
            category = input("Enter category: ")
            description = input("Enter description: ")

            t = Transaction(transaction_id, amount, transaction_type, category, description)
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
        show_pie_chart()
        
    elif choice == "6":
        show_bar_chart()
        
    elif choice == "7":
        show_monthly_trend()

    elif choice == "8":
        tracker.save_to_file() # JSON backup
        tracker.save_to_csv()  # visualization layer
        print("Goodbye! Data saved successfully.")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 8.")
