import matplotlib.pyplot as plt
import matplotlib.patheffects as pte
import numpy as np

x = np.array([1,2.5,3,4,5,6])
y = np.array([45,67,70,79,87,93])
x2 = np.array([4,5.5,2,7,1,8])
y2 = np.array([80,89,78,96,20,98]) 
plt.scatter(x,y,
            color = "Red",
            s=40,
            alpha=1,
            label="Class A"

            )

plt.scatter(x2,y2,
            color = "blue",
            s=40,
            alpha=1,
            label="Class B"

            )
plt.title("Class Comparison")
xlabell = plt.xlabel("Hours studied",fontsize=10,family="Tahoma",color="Coral")
xlabell.set_path_effects([pte.withStroke(linewidth = 2,foreground="Black")])
ylabell = plt.ylabel("Marks Attained",fontsize=10,family="Tahoma",color="lightgreen")
ylabell.set_path_effects([pte.withStroke(linewidth = 2,foreground="Black")])

plt.legend()
plt.show()