#!/bin/python3

import sys

def gemstones(arrays):
    superset = set(arrays[0])
    
    for arr in arrays[1:]:
        superset &= set(arr)
    
    return len(superset)

n = int(input().strip())
arr = []
arr_i = 0
for arr_i in range(n):
    arr_t = str(input().strip())
    arr.append(arr_t)
result = gemstones(arr)
print(result)
