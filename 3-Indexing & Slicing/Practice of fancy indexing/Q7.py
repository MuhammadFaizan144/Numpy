# 7. From a 5×5 matrix, extract values at positions (0,0), (1,2), (2,4), (3,1), (4,3).
import numpy as np
arr=np.arange(25).reshape(5,5)
row=[0 ,1, 2, 3, 4]
col=[0, 2, 4, 1, 3]
sel_val=arr[row,col]
print(sel_val)