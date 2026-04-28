# school management system
import json
from abc import ABC, abstractmethod

# -------------------------------
# Student Class
# -------------------------------

class Person(ABC):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        
    @abstractmethod
    def show_details(self):
        pass
    
# -------------------------------
# Student Class
# -------------------------------

class Student(Person):
    def __init__(self, student_id, name, age, gender, grade):
        super().__init__(name, age, gender)
        self.student_id = student_id
        self.grade = grade
        self.__attendance = 0          # private attribute
        self.__marks = {}              # private attribute
        
    # Encapsulation setters
    def update_attendance(self, days):
        if days >= 0:
            self.__attendance += days
        else:
            print("Attendance cannot be negative!")
    
    def add_marks(self, subject, mark):
        if 0 <= mark <= 100:
            self.__marks[subject] = mark
        else:
            print("Mark should be between 0 and 100.")
    
    # polymorphism -- overriding abstract method
    def show_details(self):
        return (f"Student ID: {self.student_id}\n"
                f"Name: {self.name}\n"
                f"Age: {self.age}\n"
                f"Gender: {self.gender}\n"
                f"Grade: {self.grade}\n"
                f"Attendance: {self.__attendance}\n"
                f"Marks: {self.__marks}")
        
    # Magic method
    def __str__(self):
        return f"{self.student_id} - {self.name}"
    
    # Getter for marks and attendance
    def get_attendance(self):
        return self.__attendance
    
    def get_marks(self):
        return self.__marks
    
    # method to convert to dict for JSON
    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "grade": self.grade,
            "attendance": self.__attendance,
            "marks": self.__marks
        }
        
        
# -------------------------------
# Teacher Class
# -------------------------------
class Teacher(Person):
    def __init__(self, teacher_id, name, age, gender, subject):
        super().__init__(name, age, gender)
        self.teacher_id = teacher_id
        self.subject = subject
        self.classes = []
        
    def assign_class(self, class_name):
        self.classes.append(class_name)
        
    def show_details(self):
        return (f"Teacher ID: {self.teacher_id}\n"
                f"Name: {self.name}\n"
                f"Age: {self.age}\n"
                f"Gender: {self.gender}\n"
                f"Subject: {self.subject}\n"
                f"Classes: {self.classes}")
        
    def __str__(self):
        return f"{self.teacher_id} - {self.name}"
    
    def to_dict(self):
                return {
            "teacher_id": self.teacher_id,
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "subject": self.subject,
            "classes": self.classes
        }

# -------------------------------
# School Class
# -------------------------------

class School:
    def __init__(self):
        self.students_list = []
        self.teachers_list = []
        self.load_data()
        
    # add student
    def add_student(self, student):
        self.students_list.append(student)
        
    # add teacher
    def add_teacher(self, teacher):
        self.teachers_list.append(teacher)
        
    # view all students
    def view_all_students(self):
        if not self.students_list:
            print("No Students found!")
        for student in self.students_list:
            print(student.show_details())
            print("-" * 30)
    
    # view all teachers
    def view_all_teachers(self):
        if not self.teachers_list:
            print("No teachers found!")
        for teacher in self.teachers_list:
            print(teacher.show_details())
            print("-" * 30)
            
    # save data to json
    def save_data(self):
        students_data = [student.to_dict() for student in self.students_list]
        teachers_data = [teacher.to_dict() for teacher in self.teachers_list]
        
        with open("students.json", "w") as f:
            json.dump(students_data, f, indent=4)
            
        with open("teachers.json", "w") as f:
            json.dump(teachers_data, f, indent=4)
    
    # load data from json 
    def load_data(self):
        try:
            with open("students.json", "r") as f:
                students_data = json.load(f)
                for s in students_data:
                    student = Student(
                        s["student_id"],
                        s["name"],
                        s["age"],
                        s["gender"],
                        s["grade"]
                    )
                    # restore attendance
                    student.update_attendance(s.get("attendance", 0))
                    
                    # restore marks
                    for sub, mark in s.get("marks", {}).items():
                        student.add_marks(sub, mark) 
                    self.students_list.append(student)
        except FileNotFoundError:
            pass
        
        try:
            with open("teachers.json", "r") as f:
                teachers_data = json.load(f)
                for t in teachers_data:
                    teacher = Teacher(
                        t["teacher_id"],
                        t["name"],
                        t["age"],
                        t["gender"],
                        t["subject"]
                    ) 
                    for c in t.get("classes", []):
                        teacher.assign_class(c)
                    self.teachers_list.append(teacher)
        except FileNotFoundError:
            pass
        
# -------------------------------
# Main Menu
# -------------------------------

def main_menu():
    school = School()
    while True:
        print("\n--- SCHOOL MANAGEMENT SYSTEM ---")
        print("1. Add Student")
        print("2. Add Teacher")
        print("3. Update Student Attendance")
        print("4. Add Student Marks")
        print("5. View All Students")
        print("6. View All Teachers")
        print("7. Assign Class to Teacher")
        print("8. Save & Exit")
        choice = input("Enter choice: ")   
        print()

        if choice == "1":
            try:
                sid = input("Enter Student ID: ")
                name = input("Enter Name: ")
                age = int(input("Enter Age: "))
                gender = input("Enter Gender: ")
                grade = input("Enter Grade: ")
                student = Student(sid, name, age, gender, grade)
                school.add_student(student)
                print("Student added successfully!")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "2":
            try:
                tid = input("Enter Teacher ID: ")
                name = input("Enter Name: ")
                age = int(input("Enter Age: "))
                gender = input("Enter Gender: ")
                subject = input("Enter Subject: ")
                teacher = Teacher(tid, name, age, gender, subject)
                school.add_teacher(teacher)
                print("Teacher added successfully!")
            except Exception as e:
                print(f"Error: {e}")


        elif choice == "3":
            sid = input("Enter Student ID to update attendance: ")
            student = next((s for s in school.students_list if s.student_id == sid), None)
            if student:
                try:
                    days = int(input("Enter number of days to add: "))
                    student.update_attendance(days)
                    print("Attendance updated!")
                except Exception as e:
                    print(f"Error: {e}")
            else:
                print("Student not found!")
                
        elif choice == "4":
            sid = input("Enter Student ID to add marks: ")
            student = next((s for s in school.students_list if s.student_id == sid), None)
            if student:
                try:
                    subject = input("Enter Subject: ")
                    mark = int(input("Enter marks: "))
                    student.add_marks(subject, mark)
                    print("Marks added!")
                except Exception as e: 
                    print(f"Error: {e}")
            else:
                print("Student not found!")
                
        elif choice == "5":
            school.view_all_students()
            
        elif choice == "6": 
            school.view_all_teachers()
        
        elif choice == "7": 
            tid = input("Enter Teacher ID: ")
            teacher = next((t for t in school.teachers_list if t.teacher_id == tid), None)
            if teacher:
                class_name = input("Enter class to assign: ")
                teacher.assign_class(class_name)
                print("Class assigned successfully!")
            else:
                print("Teacher not found!")
        elif choice == "8":
            school.save_data()
            print("Data saved existing...")
            break
        
        else:
            print("Invalid choice! Try again.")
            
# -------------------------------
# Run the program
# -------------------------------
if __name__ == "__main__":
    main_menu()