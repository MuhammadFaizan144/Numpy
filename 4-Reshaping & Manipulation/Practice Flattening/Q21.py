# <!-- 21. Create a 3×3 matrix and flatten it to 1D using `.flatten()` and `.ravel()` -->
import numpy as np
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr.ravel())
print(arr.flatten())