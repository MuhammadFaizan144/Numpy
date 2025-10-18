# 62. Add a 1D bias vector to a 2D matrix.
import numpy as np
arr=np.array([[1,2,3],[4,5,6]])
bias=np.array([10,20,30])
res=arr+bias
print(res)