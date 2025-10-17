# 36. Concatenate two 1D arrays `[1,2,3]` and `[4,5,6]`.
import numpy as np
arr=np.array([1,2,3])
arr1=np.array([4,5,6])
arrJoin=np.concatenate((arr,arr1))
print(arrJoin)