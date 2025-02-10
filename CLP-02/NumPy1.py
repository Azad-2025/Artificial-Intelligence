import numpy as np
matrix = np.random.randint(0, 100, (5, 5))
row_sums = np.sum(matrix, axis=1)
print("Matrix:\n", matrix)
print("Row-wise sums:", row_sums)