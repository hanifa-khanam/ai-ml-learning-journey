class Transaction:
    # class attributes
    def __init__(self, id, amount, transaction_type, category, date, description):
        self.id = id
        self.amount = amount 
        self.transaction_type = transaction_type
        self.category= category
        self.date = date
        self.description = description
        
        
    
    def __str__(self):
        return f"{self.id} - {self.transaction_type} - {self.amount} - {self.category} - {self.date} - {self.description}"
    
    def to_dict(self): 
        return {
            "Person_ID" : self.id,
            "Amount" : self.amount,
            "Type" : self.transaction_type,
            "Category" : self.category,
            "Date" : self.date,
            "Description" : self.description
        }


