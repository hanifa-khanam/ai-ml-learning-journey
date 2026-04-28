import json
from transactions import Transaction
import logging

# Configure logging
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_action(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logging.info(f"Action: {func.__name__} called")
        return result
    return wrapper



class ExpenseTracker:
    def __init__(self):
        self.transactions = []


    @log_action
    def add_transaction(self, transaction):
        """
        Add a Transaction object to the tracker.
        """
        self.transactions.append(transaction)
        print(f"Transaction {transaction.id} added successfully!")
        
    
    
    def view_transactions(self):
        """
        Print all transactions in a readable format.
        """
        if not self.transactions:
            print("No transactions found.")
            return
        for t in self.transactions:
            print(t)
            
    
    
    def save_to_file(self, filename="data.json"):
        """
        Save all transactions to a JSON file.
        """
        try: 
            with open(filename, "w") as f:
                json.dump([t.to_dict() for t in self.transactions], f, indent=4)
            print("Data saved successfully!")
        except Exception as e:
            print("Error saving data: ", e)
            
            
            
            
    def load_from_file(self, filename="data.json"):
        """
        Load transactions from a JSON file.
        """
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                for item in data:
                    t = Transaction(
                        id=item["Person_ID"], 
                        amount=item["Amount"], 
                        transaction_type=item["Type"], 
                        category=item["Category"],
                        date=item["Date"],
                        description=item["Description"]
                    )
                    self.transactions.append(t)
                print("Data Loaded Successfully!")
        except FileNotFoundError:
            print("NO previous data found. Starting fresh.")
        except Exception as e:
            print("Error loading data: ", e)
            
            
            
        
    def delete_transaction(self, transaction_id):
        """
        Delete a transaction by ID.
        """
        for t in self.transactions:
            if t.id == transaction_id:
                self.transactions.remove(t)
                print(f"Transaction {transaction_id} deleted successfully!")
                return
        print(f"No transaction found with ID {transaction_id}.")

              
    def update_transaction(self, transaction_id):
        """
        Update fields of a transaction by ID.
        """
        for t in self.transactions:
            if t.id == transaction_id:
                print("Transaction found:", t)
                
                # Ask which fields to update
                new_amount = input("Enter new amount (leave blank to keep current): ")
                if new_amount:
                    t.amount = float(new_amount)
                
                new_type = input("Enter new type (income/expense, leave blank to keep current): ")
                if new_type:
                    t.transaction_type = new_type
                
                new_category = input("Enter new category (leave blank to keep current): ")
                if new_category:
                    t.category = new_category
                
                new_date = input("Enter new date (leave blank to keep current): ")
                if new_date:
                    t.date = new_date
                
                new_description = input("Enter new description (leave blank to keep current): ")
                if new_description:
                    t.description = new_description
                
                print(f"Transaction {transaction_id} updated successfully!")
                return
        print(f"No transaction found with ID {transaction_id}.")
         



    def view_summary(self):
        total_income = 0
        total_expense = 0
        category_totals = {}

        for transaction in self.transactions:
            if transaction.transaction_type == "income":
                total_income += transaction.amount
            else:
                total_expense += transaction.amount

            # Calculate total by category
            if transaction.category not in category_totals:
                category_totals[transaction.category] = 0
            category_totals[transaction.category] += transaction.amount

        balance = total_income - total_expense

        print("\n------ Expense Summary ------")
        print(f"Total Income : {total_income}")
        print(f"Total Expense : {total_expense}")
        print(f"Balance : {balance}")
        print("\nCategory-wise totals:")
        
        for category, total in category_totals.items():
            print(f"{category}: {total}")



           
              
