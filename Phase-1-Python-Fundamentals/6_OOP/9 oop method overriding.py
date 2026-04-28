# Base class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Person constructor called")

    def introduce(self):
        print(f"Hi, I am {self.name}, and I am {self.age} years old.")

# Child class
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)  # call parent constructor
        self.subject = subject
        print("Teacher constructor called")

    def introduce(self):
        super().introduce()  # call parent method
        print(f"I teach {self.subject}.")

# Grandchild class
class Principal(Teacher):
    def __init__(self, name, age, subject, school):
        super().__init__(name, age, subject)
        self.school = school
        print("Principal constructor called")

    def introduce(self):
        super().introduce()  # use both Person + Teacher intro
        print(f"I am the principal of {self.school}.")

# Creating object
p = Principal("Hanifa", 30, "Computer Science", "Tech Valley School")
p.introduce()
