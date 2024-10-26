import numpy as np
import matplotlib.pyplot as plt
t=np.linspace(0,2*np.pi,1000)
r=1+np.cos(t)+np.sin(t)
x=r*np.cos(t)
y=r*np.sin(t)
plt.plot(x,y,color="blue",linewidth=2)
plt.fill(x,y,color="skyblue",alpha=0.7)
plt.axis("equal")
plt.axis("off")
plt.show()


