#53. Split a 4×4 array into 4 equal 2×2 blocks.
import numpy as np
arr1=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
first,second=np.split(arr1,2,axis=0)
print(first)
print(second)