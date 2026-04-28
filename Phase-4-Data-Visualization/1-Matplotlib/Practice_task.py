import matplotlib.pyplot as plt
import numpy as np

days = ["Mon", "Tue", "Wed", "Thu", "Fri"]

products = ["Laptop", "Phone", "Headphones", "Tablet"]

sales = [
    [50, 60, 55, 70, 65],   # Laptop
    [80, 85, 90, 88, 95],   # Phone
    [40, 42, 38, 45, 50],   # Headphones
    [30, 35, 33, 37, 40]    # Tablet
]

fig, ax = plt.subplots(2, 2) 

# prodcut_no = 0
# for i in range(2):
#     for j in range(2):
#         ax[i, j].plot(days, sales[prodcut_no], marker='o') 
#         ax[i, j].set_title(products[prodcut_no])
#         ax[i, j].grid(True)
#         prodcut_no += 1
        
ax = ax.flatten() 
colors = ["black", "green", "magenta", "red"]

for i, a in enumerate(ax):
    a.plot(days, sales[i], marker='o', color=colors[i], label=products[i])
    a.grid(True)
    a.legend()
    
fig.supxlabel("Days")
fig.supylabel("Units Sold")
fig.suptitle("Week Sales Analysis")
fig.tight_layout()
        
plt.show()