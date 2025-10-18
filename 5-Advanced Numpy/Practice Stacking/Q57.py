# 57. Stack two 1D arrays horizontally using `np.hstack()`.
import numpy as np
arr=np.array([1,2,3,4,5])
arr1=np.array([6,7,8,9,10])
print(np.hstack((arr,arr1)))