# """Create a contact book using a dictionary where: 
#             Key = contact name 
#             Value = phone number 
#             The user can: 
#             Add a new contact 
#             View all contacts 
#             Search for a contact 
#             Exit the program """


# contact_book = {
#     "Hanifa" : "123456789",
#     "Haris" : "987654321",
#     "Nouman" : "56323943"
# }
# while True:
#     print("\n\t\t==========WHAT YOU WANT?===========")
#     print("\t\t1. Add a new contact")
#     print("\t\t2. View all contacts") 
#     print("\t\t3. Search for a contact") 
#     print("\t\t4. Exit the program")
#     print("\t\t=====================================")

#     print("\nEnter you choice;")

#     choice = input("\nchoice (1-4): ")

#     # Option 1: add a new contact
#     if choice == "1":
#         while True:
#             print("\nContact Name: ")
#             contact = input("Enter contact name (or type 'stop' to exit): ").capitalize()
#             # if user input stop it will break and does not run again for adding contact
#             if contact == 'Stop':
#                 break 
#             print("Contact Number: ")
#             number = input("Enter phone number: ")
#             contact_book[contact] = number
#             print(f"Contact '{contact}' added successfully!")
            

#     # Option 2: view all contacts
#     elif choice == "2":
#         print("\n======Contact Book==========")
#         for key, value in contact_book.items():
#             print(f"{key}  =  {value}")

#     # Option 3: search for a contact
#     elif choice == "3":
#         print("\n===========Searching Contact============")
#         while True:
#             print("\nSearch by name;")
#             user = input("\nEnter contact name to search (or type 'Stop' to exit): ").capitalize()
#             if user == "Stop":
#                 break

#             # the found function checks if the input name is in the contact list or not
#             found = False
#             for name, number in contact_book.items():
#                 if user == name:
#                     print(f"{name}  =  {number}")
#                     found = True
#                     break
#             if not found:
#                 print(f"\n{user} not found in Contact book.")
#                 print("=====================================")
    
#     # Option 4: Exit program
#     elif choice == "4":
#         print("\nExiting the Program...............")
#         print("======================================")
#         break
#     # Invalid Option
#     else:
#         print("\nInvalid choice! Please choose between (1-4)")
#         print("================================")










"""Make a program that stores student names as keys
    and a list of subjects they study as values. 
    Allow the user to search for a student's subjects."""


info = {}
while True:
    while True:
        # taking student name as input 
        nme = input("\nEnter student name (or type 'Stop' to exit): ").capitalize()
        if nme == "Stop":
            break
        # taking student subject
        subject = (input("\nEnter student subjects separated by comma: ")).split(",")
        subject = [s.strip().capitalize() for s in subject] 

        # adding name as key and subject as value in the form of list
        info[nme] = subject
        print(f"\n Student '{nme}' added successfully!")
        print("=========================================")
        for key, value in info.items():
            print(f"{key} --> {value}")
    while True:
        # allowing user to search for a student's subject 
        print("\nDo you want to search for a Student's subject? (y/n)")
        choice = input("Choice (y/n): ").lower()
        if choice == "y":
            user = input("\nEnter student name to search: ").capitalize()
            found = False

            for key, value in info.items():
                if user == key:
                    print(f"{key} -> {value}")
                    print("========================")
                    found = True
                    break

            if not found:
                    print(f"\n{user} is not found in Student Info!")
        else:
            print("Exiting............")
            print("=====================")
            break
    print("\nDo you want to exit the program?")
    choice1 = input("Choice (y/n): ").lower()
    if choice1 == "y":
        print("\nExiting the program..............")
        print("===================================")
        break 
