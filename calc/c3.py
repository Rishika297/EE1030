import numpy as np
import matplotlib.pyplot as plt

theta= np.linspace(0,2*np.pi,400)
t=2*np.cos(theta)*np.sin(4*theta)
x=t*np.cos(theta)
y=t*np.sin(theta)
plt.plot(x,y)
plt.title(r'graph')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0,color='red',lw=0.5,ls='-')
plt.axvline(0,color='red',lw=0.5,ls='--')
plt.grid()
plt.axis('equal')
plt.show()

