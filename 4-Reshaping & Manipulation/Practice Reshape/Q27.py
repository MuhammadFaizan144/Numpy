# 27. Reshape a 1D array `[1–27]` into a 3×3×3 cube.
import numpy as np
arr=np.arange(1,28)
print(arr.reshape(3,3,3))