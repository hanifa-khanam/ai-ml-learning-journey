lines = [
    "Python is fun!\n",
    "File handling makes it powerful.\n",
    "I will master this!\n"
]

with open("motivation.txt", "w") as file:
    file.writelines(lines)

with open("motivation.txt", "r") as file:
    # print(file.read() ) # it outputs lines 
    for line in lines:
        print(line)    # it outputs in the lines form beautifully
        # print(lines)   # it outputs in the form of list