# 19. Extract the last two rows and last two columns from a 5×5 array.
import numpy as np
arr=np.array([[1,2,3,4,111],
              [5,6,7,8,222],
              [9,10,11,12,333],
              [13,14,15,16,444],
              [17,18,19,20,21]])
print(arr[-2:,-2:])