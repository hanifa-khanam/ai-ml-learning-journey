# ==========================================================
#  Author: Khanam
#  Project: Python Multi-Function Program (30 Mini Projects)
#  Description: A console-based interactive program combining
#               30 small Python applications for learning.
# ==========================================================

import random

# ==========================================================
# FUNCTIONS (1–30)
# ==========================================================

# 1. Find area of triangle
def area_of_triangle():
    print("\n========== Area of Triangle ==========")
    try:
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))
        area = 0.5 * base * height
        print(f"Area of the triangle = {area:.2f}")
    except ValueError:
        print("Invalid input! Please enter numbers only.")


# 2. Simple Calculator
def calculator():
    print("\n========== Simple Calculator ==========")
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        op = input("Choose operation (+, -, *, /, %, **): ")
        if op == '+':
            print(f"Result = {num1 + num2}")
        elif op == '-':
            print(f"Result = {num1 - num2}")
        elif op == '*':
            print(f"Result = {num1 * num2}")
        elif op == '/':
            print("Error: Division by zero." if num2 == 0 else f"Result = {num1 / num2}")
        elif op == '%':
            print(f"Result = {num1 % num2}")
        elif op == '**':
            print(f"Result = {num1 ** num2}")
        else:
            print("Invalid operator!")
    except ValueError:
        print("Invalid input! Please enter numbers only.")


# 3. Random Number Generator
def random_number():
    print("\n========== Random Number Generator ==========")
    print(f"Random number between 1–100: {random.randint(1, 100)}")


# 4. Swap Variables
def swap_variable():
    print("\n========== Swap Variables ==========")
    a = input("Enter first variable a: ")
    b = input("Enter second variable b: ")
    print(f"Before swap: a = {a}, b = {b}")
    a, b = b, a
    print(f"After swap: a = {a}, b = {b}")


# 5. ASCII Value Checker
def ascii_value():
    print("\n========== ASCII Value Checker ==========")
    ch = input("Enter a character: ")
    print(f"ASCII value of '{ch}' is {ord(ch)}" if len(ch) == 1 else "Enter only one character.")


# 6. Even or Odd
def even_odd():
    print("\n========== Even or Odd Checker ==========")
    try:
        num = int(input("Enter a number: "))
        print(f"{num} is Even." if num % 2 == 0 else f"{num} is Odd.")
    except ValueError:
        print("Please enter an integer.")


# 7. Positive or Negative
def positive_negative():
    print("\n========== Positive or Negative Checker ==========")
    try:
        num = float(input("Enter a number: "))
        if num > 0:
            print("Positive")
        elif num < 0:
            print("Negative")
        else:
            print("Zero")
    except ValueError:
        print("Invalid input!")


# 8. Complex Number Operations
def complex_number():
    print("\n========== Complex Number Operations ==========")
    try:
        real = float(input("Enter real part: "))
        imag = float(input("Enter imaginary part: "))
        num = complex(real, imag)
        print(f"Complex number: {num}")
        print(f"Conjugate: {num.conjugate()}")
        print(f"Absolute value: {abs(num)}")
    except ValueError:
        print("Invalid input!")


# 9. Leap Year Checker
def leap_year():
    print("\n========== Leap Year Checker ==========")
    try:
        year = int(input("Enter year: "))
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print("Leap Year ")
        else:
            print("Not a Leap Year ")
    except ValueError:
        print("Enter a valid year!")


# 10. Password Validation
def password_validator():
    print("\n========== Password Validator ==========")
    pwd = input("Enter a password: ")
    if (len(pwd) >= 8 and any(c.isupper() for c in pwd)
        and any(c.islower() for c in pwd)
        and any(c.isdigit() for c in pwd)
        and any(c in "!@#$%^&*()_+-=" for c in pwd)):
        print("Strong Password ")
    else:
        print("Weak Password Use mix of upper, lower, digit & symbol")


# 11. Student Grade Management
def students_data():
    students = {}
    while True:
        try:
            name = input("Enter student name: ").strip().title()
            if not name:
                raise ValueError("Name cannot be empty.")
            marks = {
                "Math": float(input("Math marks: ")),
                "English": float(input("English marks: ")),
                "Computer": float(input("Computer marks: "))
            }
            students[name] = marks
            if input("Add another student? (y/n): ").lower() == 'n':
                break
        except ValueError as e:
            print(f"Invalid input: {e}")
    return students

def calculate_average(students_dic):
    for name, subs in students_dic.items():
        avg = sum(subs.values()) / len(subs)
        print(f"{name}'s Average: {avg:.2f}")

def grade(students_dic):
    for name, subs in students_dic.items():
        avg = sum(subs.values()) / len(subs)
        if avg >= 90:
            g = "A"
        elif avg >= 80:
            g = "B"
        elif avg >= 70:
            g = "C"
        elif avg >= 60:
            g = "D"
        else:
            g = "F"
        print(f"{name} = Grade '{g}'")

def main_student_grade():
    print("\n========== Student Grade Management ==========")
    s = students_data()
    calculate_average(s)
    grade(s)


# 12. Factorial
def factorial_num():
    print("\n========== Factorial Calculator ==========")
    try:
        n = int(input("Enter number: "))
        if n < 0:
            print("Factorial not for negative numbers.")
            return
        f = 1
        for i in range(1, n+1):
            f *= i
        print(f"Factorial of {n} = {f}")
    except ValueError:
        print("Enter a valid integer.")


# 13. Multiplication Table
def multiplication_table():
    print("\n========== Multiplication Table ==========")
    try:
        num = int(input("Enter number: "))
        for i in range(1, 11):
            print(f"{num} x {i} = {num * i}")
    except ValueError:
        print("Enter a valid integer.")


# 14. Sum of Number Cubes
def sum_of_cubes():
    print("\n========== Sum of Cubes ==========")
    try:
        n = int(input("Enter a number: "))
        total = sum(i**3 for i in range(1, n+1))
        print(f"Sum of cubes till {n} = {total}")
    except ValueError:
        print("Enter a valid integer.")


# 15. Sum of Numbers
def sum_of_numbers():
    print("\n========== Sum of Numbers ==========")
    try:
        n = int(input("Enter a number: "))
        total = sum(range(1, n+1))
        print(f"Sum = {total}")
    except ValueError:
        print("Enter a valid integer.")


# 16. Prime Number Checker
def prime_checker():
    print("\n========== Prime Number Checker ==========")
    try:
        n = int(input("Enter number: "))
        if n <= 1:
            print("Not a prime number.")
        elif all(n % i != 0 for i in range(2, int(n**0.5)+1)):
            print("Prime number ")
        else:
            print("Not a prime ")
    except ValueError:
        print("Enter an integer.")


# 17. Armstrong Number Checker
def armstrong_checker():
    print("\n========== Armstrong Number Checker ==========")
    try:
        n = int(input("Enter number: "))
        s = sum(int(d)**len(str(n)) for d in str(n))
        print("Armstrong" if s == n else "Not Armstrong")
    except ValueError:
        print("Enter integer only.")


# 18. Fibonacci Sequence
def fibonacci_sequence():
    print("\n========== Fibonacci Sequence ==========")
    try:
        n = int(input("Enter number of terms: "))
        a, b = 0, 1
        for _ in range(n):
            print(a, end=" ")
            a, b = b, a + b
        print()
    except ValueError:
        print("Enter integer only.")


# 19. Disarium Number Checker
def disarium_checker():
    print("\n========== Disarium Number Checker ==========")
    try:
        n = input("Enter number: ")
        total = sum(int(d)**(i+1) for i, d in enumerate(n))
        print("Disarium " if total == int(n) else "Not Disarium")
    except ValueError:
        print("Invalid input.")


# 20. Guess the Number Game
def guess_number():
    print("\n========== Guess the Number Game ==========")
    num = random.randint(1, 50)
    while True:
        try:
            guess = int(input("Guess a number (1–50): "))
            if guess < num:
                print("Too low!")
            elif guess > num:
                print("Too high!")
            else:
                print(" Correct! You guessed it!")
                break
        except ValueError:
            print("Enter valid integer.")


# 21. Word Counter
def word_counter():
    print("\n========== Word Counter ==========")
    text = input("Enter a sentence: ")
    print(f"Word Count = {len(text.split())}")


# 22. Basic Quiz
def basic_quiz():
    print("\n========== Basic Quiz ==========")
    q = {"Python is a ___ language.": "programming",
         "C++ was developed by ___.": "bjarne stroustrup",
         "AI stands for ___.": "artificial intelligence"}
    score = 0
    for question, answer in q.items():
        user = input(question + " ").lower()
        if user == answer:
            score += 1
    print(f"You got {score}/{len(q)} correct.")


# 23. Number Reverser
def number_reverser():
    print("\n========== Number Reverser ==========")
    num = input("Enter number: ")
    print(f"Reversed: {num[::-1]}")


# 24. Temperature Converter
def temperature_converter():
    print("\n========== Temperature Converter ==========")
    try:
        c = float(input("Enter temperature in Celsius: "))
        f = (c * 9/5) + 32
        print(f"{c}°C = {f}°F")
    except ValueError:
        print("Enter valid number.")


# 25. To-Do List
def todo_list():
    print("\n========== To-Do List ==========")
    tasks = []
    while True:
        task = input("Add task (or 'done' to finish): ")
        if task.lower() == "done":
            break
        tasks.append(task)
    print("\nYour To-Do List:")
    for i, t in enumerate(tasks, 1):
        print(f"{i}. {t}")


# 26. Login System
def login_system():
    print("\n========== Login System ==========")
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == "admin" and password == "1234":
        print("Login Successful")
    else:
        print("Invalid credentials")


# 27. Palindrome Checker
def palindrome_checker():
    print("\n========== Palindrome Checker ==========")
    s = input("Enter text: ").lower()
    print("Palindrome" if s == s[::-1] else "Not Palindrome")


# 28. Interest Calculator
def interest_calculator():
    print("\n========== Interest Calculator ==========")
    try:
        p = float(input("Enter principal: "))
        r = float(input("Enter rate (%): "))
        t = float(input("Enter time (years): "))
        i = (p * r * t) / 100
        print(f"Simple Interest = {i}")
    except ValueError:
        print("Invalid input.")


# 29. Character Counter
def char_counter():
    print("\n========== Character Counter ==========")
    s = input("Enter text: ")
    print(f"Total characters (excluding spaces): {len(s.replace(' ', ''))}")


# 30. Reverse a String
def reverse_string():
    print("\n========== Reverse a String ==========")
    s = input("Enter string: ")
    print(f"Reversed: {s[::-1]}")


# ==========================================================
# MAIN MENU
# ==========================================================
while True:
    print("\n" + "="*80)
    print("🌟 PYTHON MULTI-FUNCTION PROGRAM 🌟")
    print("="*80)
    print("1. Area of Triangle\t\t11. Student Grade Management\t\t21. Word Counter")
    print("2. Calculator\t\t\t12. Factorial\t\t\t\t22. Basic Quiz")
    print("3. Random Number\t\t13. Multiplication Table\t\t23. Number Reverser")
    print("4. Swap Variables\t\t14. Sum of Cubes\t\t\t24. Temperature Converter")
    print("5. ASCII Value\t\t\t15. Sum of Numbers\t\t\t25. To-Do List")
    print("6. Even/Odd Checker\t\t16. Prime Checker\t\t\t26. Login System")
    print("7. Positive/Negative\t\t17. Armstrong Checker\t\t\t27. Palindrome Checker")
    print("8. Complex Numbers\t\t18. Fibonacci Sequence\t\t\t28. Interest Calculator")
    print("9. Leap Year Checker\t\t19. Disarium Checker\t\t\t29. Character Counter")
    print("10. Password Validator\t\t20. Guess Game\t\t\t\t30. Reverse a String")
    print("="*80)

    choice = input("Enter your choice (1–30 or 0 to Exit): ")

    functions = {
        '1': area_of_triangle, '2': calculator, '3': random_number, '4': swap_variable,
        '5': ascii_value, '6': even_odd, '7': positive_negative, '8': complex_number,
        '9': leap_year, '10': password_validator, '11': main_student_grade,
        '12': factorial_num, '13': multiplication_table, '14': sum_of_cubes,
        '15': sum_of_numbers, '16': prime_checker, '17': armstrong_checker,
        '18': fibonacci_sequence, '19': disarium_checker, '20': guess_number,
        '21': word_counter, '22': basic_quiz, '23': number_reverser,
        '24': temperature_converter, '25': todo_list, '26': login_system,
        '27': palindrome_checker, '28': interest_calculator, '29': char_counter,
        '30': reverse_string
    }

    if choice == '0':
        print("Goodbye  — Thanks for using Khanam's Python Project!")
        print("=====================================================")
        break
    elif choice in functions:
        functions[choice]()
    else:
        print("Invalid choice! Please select between 1-30 or 0 to exit.")
