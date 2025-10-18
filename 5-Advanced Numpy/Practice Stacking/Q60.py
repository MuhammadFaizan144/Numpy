# 60. Compare `stack()`, `vstack()`, and `hstack()` with examples.
import numpy as np
arr=np.array([1,2,3,4,5])
arr1=np.array([6,7,8,9,10])
print(np.stack((arr,arr1),axis=1))
import numpy as np
arr=np.array([1,2,3,4,5])
arr1=np.array([6,7,8,9,10])
print(np.vstack((arr,arr1)))
import numpy as np
arr=np.array([1,2,3,4,5])
arr1=np.array([6,7,8,9,10])
print(np.hstack((arr,arr1)))