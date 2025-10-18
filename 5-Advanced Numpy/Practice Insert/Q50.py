# 50. Insert one array into another at a specific axis.
import numpy as np
arr=np.array([[1,2,3]])
arr1=np.insert(arr,0,[99],axis=1)
print(arr1)