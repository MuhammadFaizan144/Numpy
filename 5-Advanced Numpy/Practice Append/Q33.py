# 33. Append a new column `[10,11]` to an existing (2,3) matrix.
import numpy as np
arr=np.array([[1,2,3],[4,5,6]])
arr1=np.append(arr,[[10],[11]],axis=1)
print(arr1)