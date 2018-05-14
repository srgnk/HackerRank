#!/bin/python3

import sys
from bisect import insort

def bigSorting(arr):
    return sorted(arr, key=int)
    
if __name__ == "__main__":
    n = int(input().strip())
    arr = []
    arr_i = 0
    for arr_i in range(n):
        arr_t = input().strip()
        arr.append(arr_t)
        #insort(arr, arr_t)
    result = bigSorting(arr)
    print ("\n".join(map(str, result)))
    #print ("\n".join(map(str, arr)))

