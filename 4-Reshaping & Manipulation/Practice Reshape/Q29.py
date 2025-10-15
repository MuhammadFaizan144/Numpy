# 29. Reshape a 1D array into 2D (row vector) and 2D (column vector).
import numpy as np
arr=np.array([1,2,3,4,5,6])
# row vector
print(arr.reshape(1,6))
# column vector
print(arr.reshape(6,1))
