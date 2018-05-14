#!/bin/python3

import sys

def insertionSort1(start, arr):
    probe = arr[start]
    changed = 0
    
    for ind in range(start-1, -1, -1):
        if arr[ind] > probe:
            changed += 1
            arr[ind+1] = arr[ind]
        else:
            arr[ind+1] = probe
            break
    if arr[0] > probe:
        arr[0] = probe
        
    return changed

def insertionSort2(n, arr):
    res = 0
    for ind in range(1, len(arr)):
        res += insertionSort1(ind, arr)
        #print(" ".join(map(str, arr)))
    return res

def runningTime(arr):
    return insertionSort2(len(arr), arr)
    
if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = runningTime(arr)
    print(result)
