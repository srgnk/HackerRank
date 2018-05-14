#!/bin/python3

import sys

def insertionSort1(n, arr):
    probe = arr[-1]
    
    for ind in range(len(arr)-2, -1, -1):
        if arr[ind] > probe:
            arr[ind+1] = arr[ind]
            print(" ".join(map(str, arr)))
        else:
            arr[ind+1] = probe
            print(" ".join(map(str, arr)))
            break
    if arr[0] > probe:
        arr[0] = probe
        print(" ".join(map(str, arr)))

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    insertionSort1(n, arr)
