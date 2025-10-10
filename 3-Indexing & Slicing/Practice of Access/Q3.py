# 3. Access all elements of the 2nd row of a 4×4 matrix.
import numpy as np
arr=np.array([[1,2,3,4],
             [5,6,7,8],
             [9,10,11,12],
             [13,14,15,16]])
second=arr[1, :]
print(second)