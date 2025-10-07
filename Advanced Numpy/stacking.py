"""
for stacking veryically
for stacking horizontally

vstack() row wise
hstack() column wise
its work only if both array have same amount of values
"""
import numpy as np
arr1=np.array([10,20,30])
arr2=np.array([40,50,60])
print(np.vstack((arr1,arr2)))
print(np.vstack(((arr1,arr2))))