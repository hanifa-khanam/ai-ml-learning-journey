class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        print(f"Hi, I am {self.name}, and I am {self.age} years old.")
        
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
        
    def show_details(self):
        print(f"I teach {self.subject}.")
        
class Student(Person):
    def __init__(self, name, age, roll_number):
        super().__init__(name, age)
        self.roll_number = roll_number
        
    def show_details(self):
        print(f"My roll number is {self.roll_number}.")
        
        

t1 = Teacher("Khanam", 24, "Python Programming")
t1.introduce()
t1.show_details()
s1 = Student("Hanifa", 20, "BC-120")
s1.introduce()
s1.show_details()



