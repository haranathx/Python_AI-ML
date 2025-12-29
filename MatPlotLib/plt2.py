import matplotlib.pyplot as plt
import numpy as np

x=np.array([2023,2024,2025,2026])
y1=np.array([15,25,30,20])
y2=np.array([17,23,38,5])
y3 =np.array([13,15,20,30])

# make a dictionary for the style to avoid repeat
line_style= dict(marker=".", 
                markersize=25,
                markerfacecolor="#ffbb00",
                markeredgecolor="#001100",
                linestyle="solid", # also can be dashed,dotted,dashdot,None,solid
                linewidth=4)

# Label
# Title of the plt
plt.title("Class Size", fontsize=25,
                        family="Arial",
                        fontweight="bold",
                        color="#2d4cfc")

# label of x and y axis
plt.xlabel("Year", fontsize=20,
                   family="Arial",
                   fontweight="bold",
                   color="#00ffee")
plt.ylabel("Students", fontsize=20,
                   family="Arial",
                   fontweight="bold",
                   color="#00ffee")

plt.tick_params(axis="both",
                colors="#ff4011")


plt.plot(x,y1, color="#f55b02",**line_style)

plt.plot(x,y2, color="#02f502",**line_style)

plt.plot(x,y3, color="#0298f5",**line_style)

# only show exact x axis values
plt.xticks(x)

plt.show()