import numpy as np
import matplotlib.pyplot as plt
t=np.linspace(0,2*np.pi,1000)
x=np.sin(t)
y=np.sin(t)*np.cos(t)
plt.figure(figsize=(6,6))
plt.plot(x,y,color="blue",linewidth=2)
plt.fill(x,y,color="lightblue",alpha=0.3)
plt.xlabel('x')
plt.ylabel('y')
plt.axis("equal")
plt.axis("off")
plt.show()
