# 61. Convert a 1D array into 2D row and column vector.
import numpy as np
arr=np.array([1,2,3,4,5,6])
row_vec=arr[np.newaxis,:]
col_vec=arr[:,np.newaxis]
print(row_vec)
print(col_vec)