# 44. Delete the first and last column from a 4×4 array.
import numpy as np
arr=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
new_arr=np.delete(arr,(0,3),axis=0)
print(new_arr)