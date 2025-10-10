# 10. Create two arrays `a = np.array([1,2,3,4])`, `b = np.array([0,2,3])`; use fancy indexing to extract `a[b]`.
import numpy as np
a = np.array([1,2,3,4])
b = np.array([0,2,3])
result=a[b]
print(result)