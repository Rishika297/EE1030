import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
A,B,C,D=1,2,3,4
x=np.linspace(-10,10,100)
y=np.linspace(-10,10,100)
X,Y=np.meshgrid(x,y)
Z=(-D-A*X-B*Y)/C
fig=plt.figure(figsize=(8,6))
rx=fig.add_subplot(111,projection='3d')
rx.plot_surface(X, Y, Z, color="cyan", alpha=0.5, rstride=100, cstride=100, edgecolor='k')
# Add labels and title
rx.set_xlabel("X-axis")
rx.set_ylabel("Y-axis")
rx.set_zlabel("Z-axis")
rx.set_title("3D Plane Plot")
plt.show()
