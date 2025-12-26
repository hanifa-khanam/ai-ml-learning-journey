import csv

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "Marks"])     # Header
    writer.writerow(["Hanifa", 20, 95])
    writer.writerow(["Ali", 21, 88])
    writer.writerow(["Sara", 19, 92])

print("CSV file created successfully!")









import csv

students = [
    {"Name": "Hanifa", "Age": 20, "Marks": 95},
    {"Name": "Ali", "Age": 21, "Marks": 88},
    {"Name": "Sara", "Age": 19, "Marks": 92}
]

with open("students_dict.csv", "w", newline="") as file:
    fieldnames = ["Name", "Age", "Marks"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(students)


import csv

with open("students.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
