# 51. Split `[1–10]` into two equal halves.
import numpy as np
arr1=np.arange(1, 11)
first,second=np.split(arr1,2)
print(first)
print(second)