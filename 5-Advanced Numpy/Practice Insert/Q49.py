# 49. Insert elements at multiple indices `[1,3]` in an array.
import numpy as np
arr=np.array([1,2,3,4,5])
arr1=np.insert(arr,(0,4),100)
print(arr1)