#!/bin/python3

import sys

def largestPermutation(k, arr):
    maxcur = max(arr)
    positions = {}
    
    for ind in range(len(arr)):
        positions[arr[ind]] = ind
    
    for ind in range(len(arr)):
        if k == 0:
            break
            
        if arr[ind] == maxcur:
            maxcur -= 1
            
        if arr[ind] < maxcur:
            #print("arr: {} pos: {}".format(arr, positions.items()))
            mind = positions[maxcur]
            positions[maxcur], positions[arr[ind]] = positions[arr[ind]], positions[maxcur]
            arr[ind], arr[mind] = arr[mind], arr[ind]
            #print("{} <-> {}".format(positions[maxcur], positions[arr[ind]]))
            maxcur -= 1
            k -= 1
            #print("arr: {} pos: {}".format(arr, positions.items()))
    
    return arr

if __name__ == "__main__":
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    arr = list(map(int, input().strip().split(' ')))
    result = largestPermutation(k, arr)
    print (" ".join(map(str, result)))


