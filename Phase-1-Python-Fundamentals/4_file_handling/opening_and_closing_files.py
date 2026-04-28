# with open("notes.txt", "w") as file:
#     file.write("this is my first note.")


# with open("notes.txt", "r") as file:
#     data = file.read()
#     print(data)



# # checking if the file exits before opening it using os module
# import os

# if os.path.exists("notes.txt"):
#     with open("notes.txt", "r") as file:
#         print(file.read())
# else:
#     print("File not found! Please create it first.")

# # open a file named data.txt in write mode and then close it using .close()
# file = open("data.txt", "w")
# file.write("Hello, Hanifa! Welcome to file Handling.")
# file.close()


# Use with open statement to open a dile hello.txt in write mode safely.
with open("hello.txt", "w") as file:
    print(file.write("Hey Python! i will master you soon."))



# create a program taht prints "File opened successfully" if the file opens without error.
import os
if os.path.exists("hello.txt"):
    with open("hello.txt", "r") as file:
        print(file.read())
        print("File sucessfully opened.")
else:
    print("file does not exits.")