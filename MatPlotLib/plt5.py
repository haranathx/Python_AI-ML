import matplotlib.pyplot as plt
import numpy as np

# Bar chart = Circular chart divided into slices to show percentages of the total.
#             Good for visualizing distribution among categories. 

categories = np.array(["ABC", "PQR", "123", "XYZ"])
values=np.array([300,250,275,225])
colors = ["red", "yellow", "blue", "cyan"]

plt.pie(values, labels=categories,
                autopct="%1.1f%%",
                colors=colors,
                explode=[0,0,0,0.1],
                shadow=True,
                startangle=180)

plt.title("H")

plt.show()