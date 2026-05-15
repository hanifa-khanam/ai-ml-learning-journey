from datetime import datetime
class Transaction:
    # class attributes
    def __init__(self, transaction_id, amount, transaction_type, category, description, date=None):
        self.transaction_id = transaction_id
        self.amount = amount 
        self.transaction_type = transaction_type
        self.category= category
        self.description = description
        if date is None:
            self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        else:
            self.date = date
        
    
    def __str__(self):
        return f"{self.transaction_id} - {self.transaction_type} - {self.amount} - {self.category} - {self.description} - {self.date}"
    
    def to_dict(self): 
        return {
            "Person_ID" : self.transaction_id,
            "Amount" : self.amount,
            "Type" : self.transaction_type,
            "Category" : self.category,
            "Description" : self.description,
            "Date" : self.date
        }


