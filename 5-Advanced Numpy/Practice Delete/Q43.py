# 43. Delete the 2nd row from a 3×3 array.
import numpy as np
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
new_arr=np.delete(arr,1,axis=0)
print(new_arr)