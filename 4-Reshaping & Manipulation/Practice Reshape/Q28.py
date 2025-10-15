# 28. Convert a 6×2 array into a 2×6 array using `.reshape()`.
import numpy as np
arr=np.array([[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]])
print(arr.reshape(2,6))