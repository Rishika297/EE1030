import numpy as np
import matplotlib.pyplot as plt

theta= np.linspace(0,2*np.pi,400)

r=1+np.cos(2*theta)+np.sin(2*theta)
x=r*np.cos(theta)
y=r*np.sin(theta)

plt.plot(x,y)
plt.title(r'Graph of $r=1+\cos(2\theta)+\sin(2\theta)$')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0,color='red',lw=0.5,ls='-')
plt.axvline(0,color='red',lw=0.5,ls='--')
plt.grid()
plt.axis('equal')
plt.show()

