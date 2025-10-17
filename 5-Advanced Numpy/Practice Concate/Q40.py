# 40. Concatenate arrays of different dimensions (handle reshape if needed).
import numpy as np
arr1=np.array([1,2,3])
arr2=np.array([[4,5,6]])
arr1_reshaped=arr1.reshape(1,3)
print(arr1_reshaped)
vertical_concat=np.concatenate((arr1_reshaped,arr2),axis=0)
print(vertical_concat)
horizontal_concat =np.concatenate((arr1_reshaped,arr2),axis=1)
print(horizontal_concat)