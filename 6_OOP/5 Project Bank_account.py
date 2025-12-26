class BankAccount:
    bank_name = "National Bank"
    
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        
    # method 1  introducing
    def show_info(self):
        print(f"Owner: {self.owner} | Balance: {self.balance} | Bank: {BankAccount.bank_name}")
        
    # method 2 adding balance
    def deposit(self, amount):
        if amount > 0 :
            self.balance += amount
            print(f"Deposit Successful! New balance : {self.balance}")
        else:
            print("Invalid Deposited amount.")
        
    # method 3 withdrawing balance
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal successful! New balance : {self.balance}")
        else:
            print("Invalid withdrawal or insufficient balance.")

n = BankAccount("Hanifa", 1000)
n.show_info()
n.deposit(500)
n.withdraw(200)
