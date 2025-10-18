# 64. Use broadcasting to scale each column of a 2D array by a 1D array.

import numpy as np
arr=np.array([[1,2,3],[4,5,6]])
bias=np.array([[10,20,30]])
res=arr+bias
print(res)