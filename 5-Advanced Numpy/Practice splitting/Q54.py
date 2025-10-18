#54. Use `np.array_split()` to split array unevenly.
import numpy as np
arr1=np.array([1,2,3,4,5,6])
first,second,third=np.array_split(arr1,3)
print(first)
print(second)
print(third)