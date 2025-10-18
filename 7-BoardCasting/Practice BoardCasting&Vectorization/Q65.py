# 65. Apply broadcasting to create a multiplication table (1×10, 10×1).

import numpy as np
arr=np.arange(1,11)
row=arr.reshape(1,10)
col=arr.reshape(10,1)
res=row*col

print("Row",row)
print('Column',col)
print('Result',res)