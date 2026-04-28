# """ USED TO COMPARE VALUES, 
#                         result is True or False"""
# a = 4
# b = 9
# # Equal to (==):
# print(f"{a} == {b}: ", a == b)

# # Not equal to (!=):
# print(f"{a} != {b}: ", a != b)

# # Greatr than (>):
# print(f"{a} > {b}: ", a > b)

# # Less than (<): 
# print(f"{a} < {b}: ", a < b)

# # Greater or equal to (>=):
# print(f"{a} >= {b}: ", a >= b)

# # Less or equal to (<=):
# print(f"{a} <= {b}: ", a <= b)



# while True:
#     user = (input("Enter password: ")).lower()
#     original_password = "hanifada"
#     for _ in user:
#         if user != str:
#             print("Invalid input! only letters are allowed")
#         elif user != original_password:
#             print("invalid password! try again.") 
#             user = input("Enter password again: ").lower() 
#         else:
#             print("Login successful.")
#         break



while True:
    user = input("Enter password: ").lower()
    original_password = "hanifada"

    # Check for a successful login first
    if user == original_password:
        print("Login successful.")
        break  # Exit the loop on success
    
    # Then check for invalid input
    elif not user.isalpha():
        print("Invalid input! Only letters are allowed.")

    # Otherwise, the password was just wrong
    else:
        print("Invalid password! Try again.")
