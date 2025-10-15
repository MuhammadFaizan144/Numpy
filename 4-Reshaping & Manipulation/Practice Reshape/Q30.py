# 30. Given a 2D array of shape (4,6), reshape it to (2,12).
import numpy as np
arr=np.array([[1, 2, 3, 4, 5, 6],
                [7, 8, 9, 10, 11, 12],
                [13, 14, 15, 16, 17, 18],
                [19, 20, 21, 22, 23, 24]])
print(arr.shape)
print(arr.reshape(2,12))