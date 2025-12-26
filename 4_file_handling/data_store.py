import json

file_name = "students.json"

# --- Step 1: Load existing data if file exists ---
try:
    with open(file_name, "r") as file:
        info = json.load(file)
except FileNotFoundError:
    info = {}

while True:
    while True:
        # taking student name as input 
        nme = input("\nEnter student name (or type 'Stop' to exit): ").capitalize()
        if nme == "Stop":
            break

        # taking student subjects
        subject = (input("\nEnter student subjects separated by commas: ")).split(",")
        subject = [s.strip().capitalize() for s in subject]

        # adding name as key and subject as value in dictionary
        info[nme] = subject

        print(f"\nStudent '{nme}' added successfully!")
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
                    print(f"\n{key}'s Subjects: {', '.join(value)}")
                    print("========================")
                    found = True
                    break

            if not found:
                print(f"\n{user} not found in Student Info!")
        else:
            print("\nExiting search mode............")
            print("=====================")
            break

    # --- Step 2: Save data before asking to exit ---
    with open(file_name, "w") as file:
        json.dump(info, file, indent=4)

    while True:
                #  ASK USER TO SEE EXISTING RECORDS
        if info:
            view = input("Do you want to see the stored student records? (y/n): ").lower()
            if view == "y":
                print("Existing Student Records:")
                print("=============================")
                for name, subjects in info.items():
                    print(f"{name} → {', '.join(subjects)}")
            else:
                print("Exiting view mode............")
                print("================================")
                break
        else:
            print("\nNo stored student records found yet.")
            break

    print("\nDo you want to exit the program?")
    choice1 = input("Choice (y/n): ").lower()
    if choice1 == "y":
        print("\nSaving data and exiting the program..............")
        print("===================================")
        break
