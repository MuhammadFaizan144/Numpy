# 11. Given an array from 1 to 10, filter out all even numbers.
import numpy as np
arr=np.arange(1,11)
print(arr[arr%2==0])