# text = "hello"
# encoded = text.encode("utf-8")
# print(encoded)
# decoded = encoded.decode("utf-8")
# print(decoded)






# Banking Slip using f-strings
name = "Khanam"
account = 123456789
transaction = "Deposit"
amount = 1500.75
# Banking Slip using .format()
print("\n=== Banking Slip (.format) ===")
print("Customer: {}".format(name))
print("Account No: {}".format(account))
print("Transaction: {}".format(transaction))
print("Amount: ${:.2f}".format(amount))

print("Amount: ${:>10.2f}".format(amount))  # right-align
