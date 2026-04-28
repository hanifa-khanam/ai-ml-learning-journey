class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner             # public
        self.__balance = balance       # private

    # Public method to check balance
    def show_balance(self):
        print(f"{self.owner}'s balance is: Rs {self.__balance}")

    # Public method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited Rs {amount}")
        else:
            print("Invalid deposit amount!")

    # Public method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn Rs {amount}")
        else:
            print("Invalid withdrawal or insufficient balance!")

# Object creation
account = BankAccount("Hanifa", 5000)
account.show_balance()

# Accessing public method
account.deposit(1500)
account.withdraw(2000)
account.show_balance()


