# 48. Insert a new column `[100,200]` into a (2×3) matrix.
import numpy as np
arr=np.array([[1,2,3],[4,5,6]])
arr1=np.insert(arr,1,[100,200],axis=1)
print(arr1)