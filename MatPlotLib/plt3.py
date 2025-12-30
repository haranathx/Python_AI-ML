# Grid lines

import matplotlib.pyplot as plt

# grid()= Helps make plots easy

x = [1,2,3,4,5]
y=[5,10,15,20,25]

plt.title("Grid", fontsize=20,
                   family="Arial",
                   fontweight="bold",
                   color="#00ffee")
plt.grid(axis="y", # can be "both"
         linewidth=2,
         color="#E85E13",
         linestyle="dashed")
plt.plot(x,y)

plt.show()