import numpy as np
import matplotlib.pyplot as plt
t=np.linspace(0,2*np.pi,1000)
r=1+0.9*np.sin(6*t)
x=r*np.cos(t)
y=r*np.sin(t)
plt.figure(figsize=(6,6))
plt.plot(x,y,color="purple",linewidth=2)
plt.fill(x,y,color="violet",alpha=0.3)
plt.axis("equal")
plt.axis("off")
plt.show()
