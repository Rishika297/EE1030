import numpy as np
import ctypes
func=ctypes.CDLL('/home/rishika/EE1030/assign2/codes/func.so')


if func.sub(3*B[0],2*A[0])==C[0] and func.sub(3*B[1],2*A[1])==C[1] and func.sub(3*B[2],2*A[2])==C[2] :
    print("Rank 1 and thus A,B,C collinear")
else:
    print("A,B,C not collinear")
