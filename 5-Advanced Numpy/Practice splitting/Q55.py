#55. Split a 1D array into N equal parts dynamically.
import numpy as np
arr1=np.arange(1, 11)
N=5
first=np.split(arr1,N)
for i,first  in enumerate(first,start=1):
    print(f'Part {i}:{first}')