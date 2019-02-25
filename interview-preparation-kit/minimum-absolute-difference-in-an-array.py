#!/bin/python3

import sys

def minimumAbsoluteDifference(n, arr):
    arr = sorted(arr)
    res = 10**9
    
    for ind in range(1, len(arr)):
        res = min(res, arr[ind] - arr[ind-1])
        
    return res

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = minimumAbsoluteDifference(n, arr)
    print(result)
