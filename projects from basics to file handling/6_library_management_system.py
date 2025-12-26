"""Library Management System (Mini Project)

Add, view, issue, return books

Store data in a file (JSON or CSV)

Use lists/dictionaries for records

Functions for each operation
(Perfect pre-OOP project — introduces modular design thinking)"""


import json
import os

file_name = "books.json"
books = {
    "science" : ["Biology", "Chemistry", "Physics", "Computer Science"], 
    "arts" : ["Islamiyat", "Urdu", "English"]
}

if not os.path.exists(file_name):
    with open(file_name, "w") as file:
        json.dump(books, file, indent= 4)
        print("books added successfully.")
else:
    print("Existing library loaded successfully.")
    
def add():
    with open(file_name, "r") as file:
        data = json.load(file)
        
    category = input("category name: ").strip().lower()
    new_book = input("Enter book name to add: ").title().strip()
    
    if category in data:
        data[category].append(new_book)
        if new_book not in data[category]:
            print(f"{new_book} added successfully under {category.title()}.")
        else:
            print(f"{new_book} already exists in {category.title()}.")
    else:
        data[category] = [new_book]
        print(f"New category '{category.title()}' created and '{new_book}' added.")
        
    with open(file_name, "w") as file:
        json.dump(data, file, indent= 4)
      
      
def view():
    try:
        with open(file_name, "r") as file:
            read = json.load(file)
            for category, books in read.items():
                print(f"\n{category.title()}: ")
                for book in books:
                    print(f" - {book}")
            
            
    except FileNotFoundError:
        print("file not found")
            
def issue():
    books_file = "books.json"
    issued_file = "issued_books.json"
    
    # Step 1: Load available books
    try:
        with open(books_file, "r") as file:
            available_books = json.load(file)
    except FileNotFoundError:
        print("Library file not found. Please add some books first.")
        return

    if os.path.exists(issued_file):
        with open(issued_file, "r") as file:
            try:
                issued_books = json.load(file)
            except json.JSONDecodeError:
                issued_books = {}   # file is empty or invalid
    else:
        issued_books = {}


    # Step 3: User input
    user_name = input("Enter your name: ").title().strip()
    category = input("Enter category: ").strip().lower()
    book_name = input("Enter book name: ").strip().title()

    # Step 4: Validate
    if category not in available_books:
        print(f"Category '{category.title()}' not found in library.")
        return
    if book_name not in available_books[category]:
        print(f"'{book_name}' is not available in '{category.title()}' category.")
        return

    # Step 5: Remove issued book
    available_books[category].remove(book_name)
    print(f"{user_name} has successfully issued '{book_name}' from '{category.title()}' category.")

    # Step 6: Record issued book
    if user_name in issued_books:
        if category in issued_books[user_name]:
            issued_books[user_name][category].append(book_name)
        else:
            issued_books[user_name][category] = [book_name]
    else:
        issued_books[user_name] = {category: [book_name]}

    # Step 7: Save both files
    with open(books_file, "w") as file:
        json.dump(available_books, file, indent=4)
    with open(issued_file, "w") as file:
        json.dump(issued_books, file, indent=4)

    print("Records updated successfully.")

        
def return_books():
    issued_f = "issued_books.json"
    available_f = "books.json"
    
    try:
        with open(issued_f, "r") as file:
            issued_books = json.load(file)
    except FileNotFoundError:
        print("no issued books record.")
        return
    try: 
        with open(available_f, "r") as file:
            available_books = json.load(file)
    except FileNotFoundError:
        print("Library data missing.")
        return
    
    user_name = input("Enter your name: ").strip().title()
    category = input("Enter category: ").strip().lower()
    book_name = input("Enter book_name: ").strip().title()
    
    if user_name not in issued_books:
        print(f"No records for the {user_name} found.")
        return
    elif category not in issued_books[user_name]:
        print(f"{user_name} has not issued any book from '{category}' category.")
        return
    elif book_name not in issued_books[user_name][category]:
        print(f"'{book_name}' is not issued to the user.")
        return
     # Step 5: Process return
    issued_books[user_name][category].remove(book_name)
    if category in available_books:
        available_books[category].append(book_name)
    else:
        available_books[category] = [book_name]
    
    print(f"{user_name} has successfully returned '{book_name}'.")

    # Step 6: Clean up empty records
    if not issued_books[user_name][category]:
        del issued_books[user_name][category]
    if not issued_books[user_name]:
        del issued_books[user_name]
    
    # Step 7: Save updated data
    with open(issued_f, "w") as file:
        json.dump(issued_books, file, indent=4)
    with open(available_f, "w") as file:
        json.dump(available_books, file, indent=4)
    
    print("Records updated successfully.")
while True:
    print("+++++++++++++ Main Menu ++++++++++++++")
    print("1: Add Data\n2: View data\n3: Issue books\n4: return books\n0: exit")
    choice = input("Enter your choice (1-4): ")
    if choice == '1':
        add()
    elif choice == '2':
        view()
    elif choice == '3':
        issue()
    elif choice == '4':
        return_books()
    elif choice == '0':
        print(f"Exiting library management Program.......")
        break
    else:
        print("Invalid choice!")