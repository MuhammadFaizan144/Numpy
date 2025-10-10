# 12. Extract all numbers greater than 50 from a random array of 100 elements.
import numpy as np
arr=np.arange(1,101)
print(arr[arr>50])