import numpy as np

n = int(input().strip())
array = np.array([[float(x) for x in input().strip().split()] for _ in range(n)], dtype = float)

print(np.linalg.det(array))