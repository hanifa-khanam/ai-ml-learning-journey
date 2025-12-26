# """ USED WITH BOOLEANS
#                      True / False """

# x = True
# y = False
# print("x and y is ", x and y)
# print("x or y is ", x or y)
# print("not x is ", not x)
a = 0
b = 1
if not (a and b):
    print("Hello")


if (not a) or (not b):
    print("Hello")


sunny = True
free_time = False

if sunny and free_time:
    print("Go outside 🌞")
else:
    print("Stay home 🏠")

if sunny or free_time:
    print("Go outside 🌤️")

if not sunny:
    print("Rainy mood ☔")
