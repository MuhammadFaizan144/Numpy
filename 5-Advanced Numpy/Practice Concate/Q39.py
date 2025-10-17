# 39. Create a 3×3 matrix and concatenate it with itself along both axes.
import numpy as np
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])

vertically=np.concatenate((arr,arr),axis=0)
print(vertically)
vertically=np.concatenate((arr,arr),axis=1)
print(vertically)