import matplotlib.pyplot as plt
import numpy as np

# Bar chart= compare categories of data by representing each category with a bar

categories =np.array(["Grains", "Fruit", "Vegetables", "Protein", "Dairy", "Sweet"])
values=np.array([4,3,2,5,3,1])

plt.bar(categories, values)
# if need horizontal barchart then
# plt.barh(categories, values)

plt.title("Daily Consumption")
plt.xlabel("Food")
plt.ylabel("Quantity")
plt.show()