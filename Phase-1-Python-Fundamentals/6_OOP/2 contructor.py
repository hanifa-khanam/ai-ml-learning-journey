class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price
        
    def introduce(self):
        print(f"Book: {self.title} by {self.author} - ${self.price}")
        
    def apply_discount(self, percent):
        discount = (percent / 100) * self.price
        self.price = round(self.price - discount, 2)
        print(f"Discount applied! New price: ${self.price}")

    def increase_price(self, percent):
        old_price = self.price
        increase = (percent / 100) * self.price
        self.price = round(self.price + increase, 2) 
        print(f"Price Updated from ${old_price} -> ${self.price}")
        
        
a = Book("Python Mastery", "Khanam", 25)
b = Book("OOP in Depth", "Sara", 30)

a.introduce()
b.introduce()
a.apply_discount(10)
a.introduce()
b.increase_price(10)
b.introduce()

