""" Student Grade Calculator

Take student's marks as input (use input/output, type casting)

Use if-else for grading

Store subjects and marks in lists or tuples """

print("=======Student Grade Calcultor======")
lst1 = []
while True:
    subject = input("Enter subject name (or 'done' to stop): ").title()
    if subject == 'done':
        break
    lst1.append(subject)
    
    with open("student_record.txt", "w") as file:
        file.write()
     
       
    marks = int(input("Enter marks: "))
    lst1.append(marks)
    
    print(tuple(lst1))
    
   
    
    print("Do you want to add any more? ")
    choice = input("Choice (y/n): ").lower()
    if choice == 'n':
        print("Exiting....")
        break
    