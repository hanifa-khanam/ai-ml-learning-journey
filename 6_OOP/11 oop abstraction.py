from abc import ABC, abstractmethod

# asbstract class
class Restaurant(ABC):
    def __init__(self, order_id):
        self.order_id = order_id
        
    
    @abstractmethod
    def prepare_food(self):
        pass
    
    @abstractmethod
    def pack_food(self):
        pass
    
    @abstractmethod
    def deliver_food(self):
        pass
    
    def show_order_details(self):
        print(f"Processing Order #{self.order_id}\n")
        
# child class 1
class PizzaShop(Restaurant):
    
    def prepare_food(self):
        print("Preparing Pizza dough, adding toppings, baking pizza...")
        
    def pack_food(self):
        print("Packing pizza in a cardboard box.")
        
    def deliver_food(self):
        print("Delivering pizza using fast bike delivery service.")
        
# child class 2
class BurgerShop(Restaurant):
    
    def prepare_food(self):
        print("Grilling patty, adding sauces and assembling burger...")

    def pack_food(self):
        print("Packing burger in a paper wrap with fries.")

    def deliver_food(self):
        print("Delivering burger via rider with insulated bag.")

# child class 3
class BiryaniShop(Restaurant):

    def prepare_food(self):
        print("Preparing spicy biryani with steam-cooked rice...")

    def pack_food(self):
        print("Packing biryani in sealed container.")

    def deliver_food(self):
        print("Delivering biryani safely using a delivery van.")

# polymorphism and abstraction
orders = [
    PizzaShop(order_id=101),
    BurgerShop(order_id=202),
    BiryaniShop(order_id=303)
]

for shop in orders:
    shop.show_order_details()
    shop.prepare_food()
    shop.pack_food()
    shop.deliver_food()
    print("-" * 40)