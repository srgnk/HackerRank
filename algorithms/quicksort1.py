#!/bin/python3

import sys

def quickSort(arr):
    left = []
    equal = []
    right = []
    pivot = arr[0]
    
    for el in arr:
        if el < pivot:
            left.append(el)
        elif el == pivot:
            equal.append(el)
        elif el > pivot:
            right.append(el)
            
    return left + equal + right

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = quickSort(arr)
    print (" ".join(map(str, result)))


