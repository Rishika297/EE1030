import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
t=np.linspace(0,20,1000)
x=2*t
y=3*t
z=t
fig=plt.figure(figsize=(8,6))
ax=fig.add_subplot(111,projection='3d')
ax.plot3D(x,y,z,color="blue",lw=2)
plt.show()
