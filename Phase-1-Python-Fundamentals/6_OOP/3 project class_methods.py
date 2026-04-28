"""
Classes, Objects, Constructors, Attributes, Methods, and the difference between Class vs Instance data.
"""

"""
Design a simple Student Management System that can:
Store details of multiple students
Display each student's information
Show the shared academy name
Use OOP structure (class, attributes, methods)
"""

class Student():
    academy_name = "Python Academy"
    all_students = []
    
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks
        Student.all_students.append(self)
        
    def show_details(self):
        print(f"Hi, I am {self.name}, roll number {self.roll}, and marks {self.marks} from academy {Student.academy_name}.")
        
    def update_marks(self, new_marks):
        self.marks = new_marks
        print(f"Marks Updatad for {self.name} -> {self.marks}")
        

s1 = (Student("Hanifa", 120, 89))
s2 = (Student("Amna", 130, 75))
s3 = (Student("Faiza", 140, 99))
    
class NegativeNumber(Exception):
    pass    

while True:
        
    try:
        roll_number = (input("Enter roll number to search (or 'q' to quit): "))
        if roll_number.lower() == 'q':
            print("Exiting Program....")
            break
        
        roll_number = int(roll_number)
        if roll_number < 0:
            raise NegativeNumber("Please avoid entering negative signs.")
        
        for student in Student.all_students:
            if student.roll == roll_number:
                student.show_details()
                break
        else:
            print("Student not found!")
            
    except ValueError:
        print(f"Enter roll number in numbers only.")
    except NegativeNumber as e:
        print(e)