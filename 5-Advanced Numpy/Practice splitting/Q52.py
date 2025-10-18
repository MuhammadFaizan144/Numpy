# 52. Split a 2D array into top and bottom halves.
import numpy as np
arr1=np.array([[1,2,3],[4,5,6]])
first,second=np.split(arr1,2,axis=0)
print(first)
print(second)