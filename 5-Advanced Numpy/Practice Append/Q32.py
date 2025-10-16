# 32. Append a new row `[7,8,9]` to a 2D array of shape (2,3).
import numpy as np
arr=np.array([[1,2,3],[4,5,6]])
arr2=np.append(arr,[[7,8,9]],axis=0)
print(arr2)