# 24. Given a reshaped array, flatten only selected rows.
import numpy as np
arr = np.arange(1, 13).reshape(3, 4)
print("Original array:\n", arr)
# Select specific rows (e.g., row 0 and 2)
selected_rows = arr[[0, 2]]
print("\nSelected rows:\n", selected_rows)

# Flatten only those rows
flattened_selected = selected_rows.flatten()
print(flattened_selected)