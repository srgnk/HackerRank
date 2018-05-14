#!/bin/python3

import sys

def sansaXor(arr):
    res = 0
    arr_len = len(arr)
    
    if arr_len % 2 == 0:
        return 0
    
    for ind in range(0, arr_len, 2):
        res ^= arr[ind]
        
    return res

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        arr = list(map(int, input().strip().split(' ')))
        result = sansaXor(arr)
        print(result)
