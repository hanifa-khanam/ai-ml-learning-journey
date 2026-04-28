# 🛒 1. Shopping Cart (Adding & Removing Items)
# cart = []
# # Adding items
# cart.append("Milk")
# cart.append("Bread")
# cart.insert(1, "Eggs")   # add Eggs at index 1
# print("Cart:", cart)
# # Removing items
# cart.remove("Milk")      # remove first occurrence
# print("After removing Milk:", cart)
# cart.pop()               # remove last item (Bread)
# print("After pop:", cart)


# 📋 2. To-Do List (Searching & Counting)
# tasks = ["Study", "Exercise", "Study", "Cook"]
# # Check if a task exists
# if "Exercise" in tasks:
#     print("Yes, Exercise is in the list.")
# # Count how many times "Study" appears
# print("Study appears:", tasks.count("Study"), "times")
# # Find index of "Cook"
# print("Cook is at index:", tasks.index("Cook"))


# 🏆 3. Student Ranking (Sorting & Reversing)
scores = [90, 75, 88, 100, 67]
# Sort ascending
scores.sort()
print("Sorted scores:", scores)
# Sort descending
scores.sort(reverse=True)
print("Ranked (high to low):", scores)



#📂 4. File Manager (Copying Lists)
files = ["doc1", "doc2", "doc3"]
backup = files.copy()

files.append("doc4")
print("Files:", files)
print("Backup:", backup)
