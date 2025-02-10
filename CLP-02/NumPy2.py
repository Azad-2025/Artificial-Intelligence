import numpy as np
random_values = np.random.rand(100)
normalized_values = (random_values - np.min(random_values)) / (np.max(random_values) - np.min(random_values))
print(normalized_values)