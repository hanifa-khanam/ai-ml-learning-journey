# try:
#     num = int(input("Enter a number: "))
#     result = 10 / num
# except ZeroDivisionError:
#     print("You cannot divide by zero.")
# else:
#     print("Success! The result is:", result)




# # using finally
# try:
#     num = int(input("Enter a number: "))
#     print(10 / num)
# except ZeroDivisionError:
#     print("Error: division by zero.")
# finally:
#     print("Program ended — thank you for using it!")





""" 
    Write a small program that:
Takes two numbers as input.
Divides them.
Handles both ValueError and ZeroDivisionError."""
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    division = num1 / num2
    print(f"Division of {num1} and {num2}: ", division)
except ZeroDivisionError:
    print("Cannot divided by 0.")
except ValueError:
    print("Invalid Input! Please Enter numbers only.")
else:
    print("Division completed successfully.")
finally:
    print("Program execution finished. Thank you!")





"""
Write a short program that:
Takes a number as input.
Raises an error if the number is negative (raise ValueError).
Otherwise prints “Number is valid.”
And handles the error gracefully using try-except."""
try:
    num = int(input("Enter a number: "))
    if num < 0:
        raise ValueError("Number must be positive.")
except ValueError as e:
    print("Invalid input: ", e)
else:
    print("Number is valid: ", num)




        # self.message = message
        # super()
        # .__init__(f"Enter number that is greater than 10. You enter {number} which is too small.")
            # def __init__(self, message):
            # super().__init__(message)

"""
Write a small program that:
Defines a custom exception TooSmallError.
Asks the user for a number.
Raises TooSmallError if the number is less than 10.
Handles the error gracefully using try-except.
"""

class TooSmallError(Exception):
    pass

try:
    number = int(input("Enter a number: "))
    if number < 10:
        raise TooSmallError(f"Please enter a number greater than 10. You entered {number} which is too small.")
except TooSmallError as e:
    print(e)
except ValueError:
    print("Enter numbers only.")
else:
    print(f"Successfully entered your number: ", number)