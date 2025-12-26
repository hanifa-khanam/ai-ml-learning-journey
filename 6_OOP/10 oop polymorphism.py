class Payment:
    def __init__(self, amount):
        self.amount = amount

class CreditCard(Payment):
    def process_payment(self):
        print(f"Processing PayPal payment of ${self.amount}")
        
class PayPal(Payment):
    def process_payment(self):
        print(f"Processing PayPal payment of ${self.amount}")
        
class Bitcoin(Payment):
    def process_payment(self):
        print(f"Processing Bitcoin payment of ${self.amount}")


def make_payment(payment_method):
    payment_method.process_payment()      

payments = [CreditCard(100), PayPal(250), Bitcoin(300)]
for pay in payments:
    make_payment(pay)