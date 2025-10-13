# 23. Show difference between `ravel()` (view) and `flatten()` (copy).
import numpy as np
arr = np.array([[1, 2, 3],
                [4, 5, 6]])
# Using ravel() - returns a view (changes reflect in the original array)
r=arr.ravel()
print(r)
# Using flatten() - returns a copy (changes do NOT affect the original array)
f=arr.flatten()
print(f)

# Modify the ravel array
r[0] = 100
print("\nAfter modifying ravel() array:")
print("Original array:\n", arr)

# Modify the ravel array
f[1] = 100
print("\nAfter modifying flatten() array:")
print("Original array:\n", arr)
