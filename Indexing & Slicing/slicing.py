"""
slicing
array[start,stop,step]
arr[start:end] , start to end - 1
negative step, -1 reverse
"""
import numpy as np
arr =np.array([1,2,3,4,5,6])
print(arr[0:5])
print(arr[:4])
print(arr[::2])
print(arr[::-1])