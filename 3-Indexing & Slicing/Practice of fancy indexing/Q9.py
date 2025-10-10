# 9. Replace elements at indices `[1, 3, 4]` in an array with `0`.
import numpy as np
arr= np.array([1,2,4,5,6,7,4])
arr[[1,3,4]]=0
print(arr)