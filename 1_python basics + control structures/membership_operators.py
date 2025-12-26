""" TO CHECK WHETHER VALUE EXISTS
                        INSIDE STRING, LIST, TUPLE, SET, DICTIONARY. """

# USING in operator
a = "hanifadawar"
vowels = '("a", "e", "i", "o", "u")'
for v in vowels:
    if v in a:
        print(f"Yes, {v} is in {a} ")




marks = int(input("\nEnter  obtained marks: ")) 
total = int(input("Enter total marks: "))
percent = ((marks) / (total)) * 100
print(
"\n****  GRADE ****")
match percent:
    case  percent if percent >= 90:
        print(f" Obtained Marks = {marks} \n Total Marks = {total} \n  percentage {percent}% \n Grade: 'A'.")
    case percent if percent >=  80:
        print(f" Obtained Marks = {marks} \n Total Marks = {total} \n  percentage {percent}% \n Grade: 'B'.")
    case percent if percent >= 70:
        print(f" Obtained Marks = {marks} \n Total Marks = {total} \n  percentage {percent}% \n Grade: 'C'.")
    case  percent if percent >= 60:
        print(f" Obtained Marks = {marks} \n Total Marks = {total} \n  percentage {percent}% \n Grade: 'D'.")
    case percent if percent >= 50:
        print(f" Obtained Marks = {marks} \n Total Marks = {total} \n  percentage {percent}% \n Grade: 'E'.")
    case _ :
        print(f" Obtained Marks = {marks}  \n Total Marks = {total} \n  percentage {percent}% \n Grade: 'fail'.") 

