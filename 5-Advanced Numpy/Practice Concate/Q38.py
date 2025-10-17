# 38. Concatenate three 1D arrays into one.
import numpy as np
arr=np.array([1,2,3])
arr1=np.array([4,5,6])
arr2=np.array([7,8,9])
arrJoin=np.concatenate((arr,arr1,arr2))
print(arrJoin)