# print("""\n Student Management Console App (Beginner Level Project)
# Concepts Covered:
#  Basics
#  Control Structures
#  Strings
#  Lists
#  Tuples
#  Sets
#  Dictionaries""")

"""Project Goal:

Build a small console-based program that can:

            Add new students.

            View all students.

            Search a student by name.

            Show unique courses (using sets).

            Exit the program safely."""
# student data
student = {
    "Hanifa" : ['AI', 'ML', 'Python', 'Software Engineering'],
    "Nouman" : ['AI', 'ML', 'Data structure and Algorithm'],
    "Haris" : ['Soft skills', 'NEBOSH', 'IOSH'],
    "Raheela" : ['AI', 'Python', 'Communication skills']
}

while True:
    print("\n\t\t\t\t=====Student Management Main Menu=====")
    print("\t\t\t\t1. Add new students")
    print("\t\t\t\t2. View all students")
    print("\t\t\t\t3. Search a student by name")
    print("\t\t\t\t4. Show unique courses")
    print("\t\t\t\t0. Exit the Program")
    print("\t\t\t\t==========================================")
    
    # taking choice from user
    print("\nEnter your choice;")
    choice = input("choice (0-4): ")
    if choice == '1':
        print("\n\t\t====Add New Student===")
        while True:
            name = input("\nEnter student name (or type 'Stop' to exit): ").title()
            # if user type stop then no more student then will add
            if name == 'Stop':
                print("==============================================")
                break
            # taking courses of student from the user
            subject = input("Enter student courses separated by commas: ").split(",")
            # converting the input courses in list
            course = [s.strip().title() for s in subject]
            # adding input name as key and course as value in the form of list in dictionary
            student[name] = course
            #showing that student is added successfully
            print(f"{name} added Successfully.")
            print("=======================================================")
    
        
    elif choice == '2':
        print("\n\t====View All Student====")
       # looping through dictionary so student name and their courses will be displayed
        for  k, v in student.items():
            print(f"\n{k} = {v}")
        print("========================================================")
        
    elif choice == '3':
        print("\n=====Search student by name=====")
        while True:
            user = input("\nEnter Student Name (or type 'stop' to exit): ").title()
            # if user type stop then no more searching
            if user == "Stop":
                print("===========================================================")
                break
            
			# found will check that user input name exist in student dictionary or not
            found = False
            for key, vlaue in student.items():
                # if exist it will print student name and his/her courses
                if key == user:
                    print(f"\n{key} = {vlaue}")
                    print("=============================================")
                    found = True
                    break
            # if name not present it will print not found
            if not found:
                print(f"\n{user} is not found in student data.")
                print("======================================")
                
    elif choice == '4':
        print("\n=====Unique courses=====")

        unique_courses = set()
        
        for v in student.values():
            # it will convert values (list of courses) in a set
            unique_courses.update(v)
        for c in sorted(unique_courses):
            print(c)   
        print("=====================")
          
    elif choice == '0':
        print("\nExiting the program............")  
        print("==================================")
        break
    
    else:
        print("\nInvalid Choice! choose between (0-4).")
        print("========================================")
        

        
                
                
            
                
        

     



