import numpy as np
import ctypes
func=ctypes.CDLL('/home/rishika/EE1030/assign3/codes/func.so')
A=[1,0]
B=[0,1]
if A[0]==B[1]:
    print("slope of the line is -1")
else:
    print("slope of the line is not equal to -1")


