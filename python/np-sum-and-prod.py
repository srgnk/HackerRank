import numpy as np

n, m = map(int, input().split())
print(np.prod(np.sum(np.array([input().split() for _ in range(n)],int), axis = 0)))
