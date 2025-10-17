# 37. Concatenate two 2D arrays vertically and horizontally.
import numpy as np
arr=np.array([[1,2,3]])
arr1=np.array([[4,5,6]])
vertical=np.concatenate((arr,arr1),axis=0)
print(vertical)
horizontally=np.concatenate((arr.T,arr1.T),axis=1)
print(horizontally)