import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-10,10,100)
y=x**2
plt.plot(x,y,label=r'$y=x^2$')
plt.xlabel(r'$x$(input)',fontsize=12)
plt.ylabel(r'$y$(output)',fontsize=12)
plt.title(r'Graph of $y=x^2$',fontsize=14)
plt.legend()
plt.grid(True)
plt.show()
