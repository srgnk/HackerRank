import numpy as np

array = np.array(list(map(float, input().strip().split())))
x = float(input().strip())

print(np.polyval(array, x))
