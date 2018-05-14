import numpy as np

array = np.array(list(input().strip().split()), dtype = float)
                 
print(np.floor(array))
print(np.ceil(array))
print(np.rint(array))