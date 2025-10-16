# 35. Append values only if they are not already in array.
import numpy as np
arr=np.array([1,2,3,4,5,6])
new_value=np.array([3,5,6,7])
for val in new_value:
    if val not in arr:
        arr=np.append(arr,val)
print(arr)