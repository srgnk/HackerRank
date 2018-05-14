import numpy as np

n, m = [int(x) for x in input().strip().split()]
array = np.array([[int(x) for x in input().strip().split()] for _ in range(n)])
print(np.prod(np.sum(array, axis = 0)))