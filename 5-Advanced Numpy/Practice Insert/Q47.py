# 47. Insert `[10,20,30]` as a new row into a (2×3) matrix.
import numpy as np
arr=np.array([[1,2,3],[4,5,6]])
arr1=np.insert(arr,1,[10,20,30],axis=0)
print(arr1)