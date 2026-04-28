class Student():
    university_name = "Virtual University of Pakistan"
    all_students = []
    
    def __init__(self, name, roll, cgpa):
        self.name = name
        self.roll = roll
        self.cgpa = cgpa
        Student.all_students.append(self)
        
    
    def introduce(self):
        print(f"\nAssalam-o-Alaikum! I am {self.name}")
        print(f"From {Student.university_name} having ID {self.roll}")
        print(f"I have got CGPA {self.cgpa} out of 4.\nThank you..")
        
        
    def update_marks(self, new_marks):
        self.cgpa = new_marks
        print(f"Marks updated for {self.name} = {self.cgpa}")
        

# Custom Exception
class NegativeNumbers(Exception): pass
class NumberValueError(Exception): pass
class OutLimitedError(Exception): pass

# pre added students
s1 = Student("Hanifa", 250, 3.63)
s2 = Student("Naima", 220, 3.89)

while True:
    print("\n===== MENU =====")
    print("1. Add Student")
    print("2. Show All Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Exit")
    
    user = input("Enter your choice (1-5): ") 
    
    if user == "1":
        print("\nAdding Student: ")
        try:
            name = input("Enter Student name: ").title()
            if name.isnumeric() or name.strip() == "":
                raise NumberValueError("Kindly enter letters only not numbers or empty spaces!")
            
            roll = int(input("Enter student roll number: "))
            if roll < 0:
                raise NegativeNumbers("Kindly enter positive numbers only.")
            
            cgpa = float(input("Enter student CGPA: "))
            if cgpa <= 0 or cgpa > 4.0:
                    raise  OutLimitedError("Kindly enter CGPA greater than 1.0 and <= 4.0.")
                
            Student(name, roll, cgpa)
            print(f"{name} as Student added successfully.")
            
        except (NumberValueError, NegativeNumbers, OutLimitedError) as e:
            print(e)

            
    # showing all students name
    elif user == "2":
        if not Student.all_students:
            print("\nNo students available yet.")
        else:
            print("\nList of Students:")
            for student in Student.all_students:
                print(f"-{student.name} --> Roll Number {student.roll} --> CGPA {student.cgpa}")
    
    # searching by student name to introduce that student
    elif user == "3":
        try:
            s_name = input("Enter student name to search: ").title()
            if s_name.isdigit() or s_name.isnumeric() or s_name.isdecimal():
                raise NumberValueError("Kindly enter letters only not numbers!")
        
            for student in Student.all_students:
                if  student.name.lower() == s_name.lower():
                    student.introduce()
                    break
            else:
                print("Student not found!")
                
        except NumberValueError as e:
            print(e)
            
    # entering roll number for updating marks    
    elif user == "4":
        try:
            roll_number = int(input("Enter student roll number to update marks: "))
            if roll_number < 0:
                raise NegativeNumbers("Kindly enter positive numbers only.")
            
            for student in Student.all_students:
                if student.roll == roll_number:
                    updated_cgpa = float(input("Enter updated CGPA: "))
                    if updated_cgpa <= 0 or updated_cgpa > 4.0:
                        raise  OutLimitedError("Kindly enter CGPA greater than 1.0 and <= 4.0.")
                    student.update_marks(updated_cgpa)
                    break
            else:
                print(f"Student not found having roll number {roll_number}")
                
        except (NegativeNumbers, OutLimitedError) as e:
            print(e)

    elif user == "5":
        print("Exiting Program...")
        print()
        break
    
    else:
        print("Invalid choice! Please enter a number between 1-5.")
        print()
    
    
    
    
    