#!/bin/python3

import sys

def insertionSort1(start, arr):
    probe = arr[start]
    
    for ind in range(start-1, -1, -1):
        if arr[ind] > probe:
            arr[ind+1] = arr[ind]
        else:
            arr[ind+1] = probe
            break
    if arr[0] > probe:
        arr[0] = probe

def insertionSort2(n, arr):
    for ind in range(1, len(arr)):
        insertionSort1(ind, arr)
        print(" ".join(map(str, arr)))

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    insertionSort2(n, arr)
