"""
np.delete(array,index,axis=none)
flattern array
"""

import numpy as np
arr=np.array([10,20,30,40,50])
new_arr=np.delete(arr,(2))
print(new_arr)