import numpy as np
import ctypes
func=ctypes.CDLL('/home/rishika/EE1030/assign2/codes/func.so')
A=[-2,3]
B=[6,7]
C=[8,3]
D=[0,-1]
if func.add(func.sub(A[0],B[0]),C[0])==D[0] or func.add(func.sub(A[1],B[1]),C[1])==D[1]:
    print("D(0,-1) is the fourth vertex of the parallelogram")
else:
    print("D(0,-1) is not the fourth vertex of the parallelogram")

