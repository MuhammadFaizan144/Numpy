# 45. Delete a row or column using slicing instead of `np.delete()`.
import numpy as np
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
arr_without_row = np.vstack((arr[:1, :], arr[2:, :]))
arr_without_column=np.hstack((arr[:,:1],arr[:,2:]))
print(arr_without_row)
print(arr_without_column)