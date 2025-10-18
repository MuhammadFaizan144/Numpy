# 58. Use `np.column_stack()` to merge column-wise.
import numpy as np
arr=np.array([1,2,3,4,5])
arr1=np.array([6,7,8,9,10])
print(np.column_stack((arr,arr1)))