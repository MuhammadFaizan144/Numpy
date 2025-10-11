# 13. Create an array of random integers and filter elements divisible by 5.
import numpy as np
arr=np.random.randint(1,101,size=20)
print(arr)
arr_5=arr[arr%5==0]
print(arr_5)