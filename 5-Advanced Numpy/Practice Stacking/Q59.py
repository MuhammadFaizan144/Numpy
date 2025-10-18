# 59. Stack multiple small arrays into a 3D array.
import numpy as np
arr=np.array([1,2,3,4,5])
arr1=np.array([6,7,8,9,10])
arr2=np.array([6,7,8,9,10])
stack3d=np.stack((arr,arr1,arr2),axis=0)
print(stack3d.shape)