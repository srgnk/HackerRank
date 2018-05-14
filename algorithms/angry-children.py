#!/bin/python3

import sys

def angryChildren(k, arr):
    arr = sorted(arr)
    res = arr[-1]
    
    for ind in range(len(arr)-k+1):
        res = min(res, arr[ind+k-1] - arr[ind])
        #print("ind = {} arr = {} res = {}".format(ind, arr[ind:ind+k], res))
    
    return res
    

if __name__ == "__main__":
    n = int(input().strip())
    k = int(input().strip())
    arr = []
    arr_i = 0
    for arr_i in range(n):
        arr_t = int(input().strip())
        arr.append(arr_t)
    result = angryChildren(k, arr)
    print(result)
