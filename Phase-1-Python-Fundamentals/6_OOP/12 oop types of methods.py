class Student:
    school_name = "Digital School"
    student_count = 0  # class variable

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        Student.student_count += 1  # counting objects
    
    # instance method
    def show_details(self):
        print(f"Student Name: {self.name}, Grade: {self.grade}")

    # class method
    @classmethod
    def get_total_students(cls):
        return f"Total students: {cls.student_count}"

    @classmethod
    def change_school_name(cls, new_name):
        cls.school_name = new_name
        print("School name updated!")
    @classmethod
    def create_student_from_string(cls, data):
        name, grade = data.split("-")
        grade = int(grade)
        return cls(name, grade)
    
    # static method
    @staticmethod
    def school_rules():
        print("School starts at 8 AM and ends at 2 PM.")


# Using the class
s1 = Student("Hanifa", 10)
s2 = Student("Ali", 9)

s1.show_details()
s2.show_details()

s3 = Student.create_student_from_string("Sara-11")
s3.show_details()


print(Student.get_total_students())

Student.change_school_name("Python International School")
print(Student.school_name)

Student.school_rules()
