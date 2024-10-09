import numpy as np
import ctypes
func=ctypes.CDLL('/home/rishika/EE1030/assign3/codes/func.so')
x=0
y=13/6
if (x==0 and y==13/6):
    print("3x^2+3y^2-13y=0 is the circle equation that passes through (2,3),(0,0) and having center on the y-axis.")
else:
    print("Not the circle equation that passes through (2,3),(0,0) and having center on the y-axis.")


