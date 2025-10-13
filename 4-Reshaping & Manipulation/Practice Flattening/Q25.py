# 25. Convert a 2D array into a list using flattening.
import numpy as np
# Create a 2D array
arr = np.array([[10, 20, 30],
                [40, 50, 60]])

print("Original array:\n", arr)

# Flatten the array and convert it into a list
list_from_array = arr.flatten().tolist()
print(list_from_array)