# 22. Flatten a 3D array of shape (2,3,4) and verify total number of elements.
import numpy as np
arr=np.arange(24).reshape(2,3,4)
flat=arr.flatten()
print(arr.shape)
print(flat)
print(flat.size)