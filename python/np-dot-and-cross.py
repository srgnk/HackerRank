import numpy as np

n = int(input().strip())
arr1 = np.array([[int(x) for x in input().strip().split()] for _ in range(n)])
arr2 = np.array([[int(x) for x in input().strip().split()] for _ in range(n)])

print(np.dot(arr1, arr2))