class Student():
    school_name = "Digital School"    # class attribute
    
    def __init__(self, name, roll, grade):
        self.name = name
        self.roll = roll
        self.grade = grade
        self.grade += 1
        
s1 = Student("Hanifa", 120, 12)
s2 = Student("Nouman", 140, 13)
s3 = Student("Awais", 12, 9)

print(Student.school_name)
print(s1.__dict__)





# class Student:
#     school_name = "Python Academy"
#     def __init__(self, name, roll, marks):
#         self.name = name
#         self.roll = roll
#         self.marks = marks

# # create 2 students
# s1 = Student("Hanifa", 120, 89)
# s2 = Student("Awais", 130, 75)

# # print individual data
# print(s1.name, s1.roll, s1.marks)
# print(s2.name, s2.roll, s2.marks)

# # print school name from both
# print(s1.school_name)
# print(s2.school_name)

# # print both namespaces
# print(s1.__dict__)
# print(s2.__dict__)

# s1.school_name = "AI Academy"
# print(s1.school_name)
# print(s2.school_name)
# print(Student.school_name)






