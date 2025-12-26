class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    # Print object nicely
    def __str__(self):
        return f"Student({self.name}, Marks: {self.marks})"

    # len(object) → return marks count
    def __len__(self):
        return len(self.marks)

    # Adding two students → combine marks
    def __add__(self, other):
        return self.marks + other.marks

    # Comparing students by marks total
    def __eq__(self, other):
        return sum(self.marks) == sum(other.marks)


# Testing
s1 = Student("Hanifa", [90, 85, 88])
s2 = Student("Ali", [80, 85, 90])

print(s1)         # __str__
print(len(s1))    # __len__
print(s1 + s2)    # __add__
print(s1 == s2)   # __eq__
