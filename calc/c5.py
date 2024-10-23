import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,2*np.pi,100)
ys=np.sin(x)
yc=np.cos(x)
plt.plot(x,ys)
plt.plot(x,yc)
plt.legend()
plt.show()
