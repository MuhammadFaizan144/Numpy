# 63. Multiply a 1D array with a 2D array using broadcasting.
import numpy as np
arr=np.array([[1,2,3],[4,5,6]])
bias=np.array([10,20,30])
res=arr*bias
print(res)